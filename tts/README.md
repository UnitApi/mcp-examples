# Text-to-Speech (TTS) Examples

Przykłady integracji MCP Hardware z syntezą mowy (Text-to-Speech) oraz zdalnym uruchamianiem serwera TTS.

## Pliki
- `tts_server.py` — Serwer MCP, który odbiera tekst i odtwarza go na głośniku komputera (pyttsx3, endpoint HTTP /tts).
- `tts_client_ollama.py` — Klient pobierający prognozę pogody z modelu Ollama i wysyłający ją do serwera TTS.
- `tts_server_runner.py` — Skrypt uruchamiający serwer TTS na zdalnym urządzeniu przez SSH (wymaga paramiko).

## Uruchomienie lokalne
1. Uruchom serwer TTS:
   ```bash
   python tts_server.py
   ```
2. Uruchom klienta (wymaga działającego serwera Ollama):
   ```bash
   python tts_client_ollama.py
   ```

## Uruchomienie serwera TTS na zdalnym urządzeniu przez SSH
1. Skopiuj `tts_server.py` na zdalny komputer (np. Raspberry Pi).
2. Użyj runnera:
   ```bash
   python tts_server_runner.py <adres_ssh> -u <użytkownik> -p <ścieżka_do_tts_server.py>
   ```
   Przykład:
   ```bash
   python tts_server_runner.py 192.168.1.100 -u pi -p /home/pi/UnitApi/mcp/examples/tts/tts_server.py
   ```

## Wymagania
- Python 3
- `pyttsx3` (na serwerze TTS)
- `aiohttp` (na serwerze TTS)
- `paramiko` (na komputerze uruchamiającym runnera)
- `requests` (na kliencie)

## Opis działania
- Serwer nasłuchuje na porcie 8081 i odtwarza przesłany tekst na głośniku.
- Klient pobiera prognozę pogody z lokalnego modelu Ollama (endpoint http://localhost:11434/api/generate) i przesyła ją do serwera TTS.
- Runner pozwala uruchomić serwer TTS na zdalnym urządzeniu przez SSH.

Każdy plik można uruchomić osobno zgodnie z powyższą instrukcją.
