# Protean-AI-nanda
NANDA-wrapped AI agent with intent detection

AI agent with intent detection, wrapped with NANDA Adapter for A2A communication.

## Agent Information
- **Name**: adet.adel agent  
- **Status**: Active ✅
- **NANDA Certified**: Yes
- **Endpoint**: https://api.aoaprotean.net

## Features
- Intent detection (search, analysis, meal planning)
- 24/7 operation on AWS EC2
- A2A protocol compatible

## Files
- `protean_agent.py` - Main agent code
- `adapter.env.example` - Configuration template
- `nanda-example.service` - Systemd service file


## Setup
1. Copy `adapter.env.example` to `/etc/protean/adapter.env`
2. Add your Anthropic API key
3. Install service: `sudo cp nanda-example.service /etc/systemd/system/`
4. Start: `sudo systemctl start nanda-example.service`

## Author
Adetola Adeleke
