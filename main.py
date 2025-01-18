import grpc
import logging
import json
import base64
import requests
import uuid
from flask import Flask, request, jsonify
from gigachat_pb2 import ChatRequest, Message, ChatOptions
from gigachat_pb2_grpc import ChatServiceStub

# Настройка логирования
logging.basicConfig(level=logging.DEBUG)

# Конфигурация GigaChat gRPC
GRPC_SERVER_ADDRESS = "gigachat.devices.sberbank.ru:443"
CA_BUNDLE_FILE = "russian_trusted_root_ca.cer"
AUTH_URL = "https://ngw.devices.sberbank.ru:9443/api/v2/oauth"
STATIC_BEARER_TOKEN = ""

# Flask приложение
app = Flask(__name__)

class GigaChatClient:
    def __init__(self, ca_bundle_file):
        self.ca_bundle_file = ca_bundle_file
        self.token = self.refresh_token()
        self.channel = grpc.secure_channel(
            GRPC_SERVER_ADDRESS,
            grpc.ssl_channel_credentials(root_certificates=open(ca_bundle_file, "rb").read())
        )
        self.stub = ChatServiceStub(self.channel)

    def refresh_token(self):
        """Получение нового токена доступа"""
        headers = {
            "Authorization": f"Basic {STATIC_BEARER_TOKEN}",
            "Content-Type": "application/x-www-form-urlencoded",
            "Accept": "application/json",
            "RqUID": str(uuid.uuid4()),
        }
        data = {"scope": "GIGACHAT_API_PERS"}
        response = requests.post(AUTH_URL, headers=headers, data=data, verify=False)
        if response.status_code == 200:
            token = response.json().get("access_token")
            logging.info(f"New Access Token retrieved: {token}")
            return token
        else:
            logging.error(f"Failed to retrieve Access Token: {response.text}")
            raise Exception("Failed to retrieve Access Token")

    def chat(self, text):
        """Отправка запроса в GigaChat"""
        metadata = [("authorization", f"Bearer {self.token}")]
        options = ChatOptions(
            temperature=0.7,
            top_p=0.9,
            max_tokens=100,
            repetition_penalty=1.0
        )
        request = ChatRequest(
            model="GigaChat-Pro",
            options=options,
            messages=[
                Message(role="system", content="ты отыгрываешь роли персоонажей в ролевой игре Morrowind, присланные тебе фразы это стандартные реплики npc из игры, надо их перфразирововать, при этом все слова которые отмечены специальными символами @ и # должны остаться во фразе,без изменений с этими же символами"),
                Message(role="user", content=text)
            ]
        )
        try:
            logging.info(f"Sending request to GigaChat: {request}")
            logging.info(f"Metadata: {metadata}")
            response = self.stub.Chat(request, metadata=metadata)
            return response.alternatives[0].message.content if response.alternatives else ""
        except grpc.RpcError as e:
            if e.code() == grpc.StatusCode.UNAUTHENTICATED:
                logging.warning("Access Token expired. Refreshing...")
                self.token = self.refresh_token()
                metadata = [("authorization", f"Bearer {self.token}")]
                response = self.stub.Chat(request, metadata=metadata)
                return response.alternatives[0].message.content if response.alternatives else ""
            logging.error(f"gRPC error: {e.details()} (code: {e.code()})")
            raise

# Инициализация gRPC клиента
gigachat_client = GigaChatClient(CA_BUNDLE_FILE)

@app.route("/<dialogue_type>", methods=["POST"])
def handle_dialogue(dialogue_type):
    if dialogue_type not in ["greeting", "dialogue"]:
        logging.error(f"Unsupported dialogue type: {dialogue_type}")
        return jsonify({"error": "Unsupported dialogue type"}), 404

    try:
        # Декодируем входящие данные
        raw_data = request.data.decode("cp1251")
        logging.info(f"[{dialogue_type}] Raw request data: {raw_data}")
        data = json.loads(raw_data)

        # Проверяем, что текст передан
        if "text" not in data:
            logging.error(f"Missing 'text' field in request data: {data}")
            return jsonify({"error": "Missing 'text' field"}), 400

        original_text = data["text"]
        logging.info(f"Original text: {original_text}")

        # Отправляем запрос в GigaChat
        modified_text = gigachat_client.chat(original_text)
        logging.info(f"Modified text: {modified_text}")

        # Возвращаем текст обратно клиенту в cp1251
        return modified_text.encode("cp1251"), 200, {"Content-Type": "text/plain; charset=cp1251"}

    except Exception as e:
        logging.error(f"[{dialogue_type}] Error: {e}")
        return jsonify({"error": "Internal server error"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
