#!PLASEHOLDER!ПРИМЕР! LLMaster: Framework for NPC Dialogue Rephrasing

**LLMaster** is a universal tool for integrating Large Language Models (LLMs) into video games, specifically to enhance NPC dialogue with role-playing potential. The framework supports cloud-based and local models, enabling seamless connection and role-play generation for NPCs.

## Features

- **Multi-provider Support**: Integrates with cloud providers like OpenAI, Sber GigaChat, and local models via tools like Ollama.
- **Dynamic Dialogue Rephrasing**: Enhances NPC dialogue to be engaging while preserving essential markers.
- **Game Agnostic**: Can be adapted for any game engine or framework.
- **Customizable Role-Playing Rules**: Define specific NPC behaviors, including rules for special tokens like `@` and `#`.
- **Efficient Caching**: Reduces latency by caching responses.

---

## Project Structure

```plaintext
├── server/
│   ├── main.py           # Flask server for processing game dialogue
│   ├── grpc_client.py    # gRPC client for GigaChat integration
│   ├── ollama_client.py  # Local model integration via Ollama
│   ├── utils/            # Utility functions
├── client/
│   ├── morrowind.lua     # Example MWSE Lua integration for Morrowind
├── docs/
│   ├── README.md         # Documentation
├── configs/
│   ├── settings.json     # Model settings and API keys
├── tests/
│   ├── test_server.py    # Unit tests for Flask server
```

---

## Getting Started

### Prerequisites

1. **Python Environment**: Python 3.9 or higher.
2. **Game Environment**: Example uses Morrowind Script Extender (MWSE).
3. **API Access**:
   - OpenAI or similar provider for LLM.
   - CA certificates for GigaChat integration.

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/username/llmaster.git
   cd llmaster
   ```

2. Set up a virtual environment and install dependencies:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Configure API keys and settings in `configs/settings.json`:
   ```json
   {
     "openai_api_key": "your_openai_key",
     "grpc_address": "gigachat.devices.sberbank.ru:443",
     "ollama_path": "path/to/ollama"
   }
   ```

4. Run the Flask server:
   ```bash
   python server/main.py
   ```

5. Add `client/morrowind.lua` to your MWSE mods folder for integration.

---

## Usage

### Game Integration

NPC dialogue is intercepted by the game client and sent to the Flask server in JSON format. The server processes the request and connects to the specified LLM for rephrasing.

Example JSON format:
```json
{
  "text": "@Hero# is needed to save the world!",
  "npc": "Guard",
  "context": "Greeting"
}
```

Server response:
```json
{
  "text": "@Hero#, your help is essential to protect us from disaster!"
}
```

### Supported Providers

- **OpenAI**: Flexible support for GPT-4o and GPT-4o-mini.
- **Sber GigaChat**: Via gRPC.
- **Ollama**: Local LLM integration.

---

## Contributing

We welcome contributions! Please fork the repository, make your changes, and submit a pull request.

### Development

1. Install development dependencies:
   ```bash
   pip install -r requirements-dev.txt
   ```
2. Run unit tests:
   ```bash
   pytest tests/
   ```

---

## Roadmap

- [ ] Add support for additional cloud providers (AWS Bedrock, Azure OpenAI).
- [ ] Expand example integrations to other game engines (Unity, Unreal Engine).
- [ ] Advanced dialogue caching for low-latency responses.
- [ ] Add model benchmarking and analytics.

---

## License

This project is licensed under the MIT License. See `LICENSE` for details.

---

## Acknowledgements

Special thanks to the creators of MWSE, Flask, and the wider modding and gaming community for inspiration and support.

For questions or support, please contact [your_email@example.com].

