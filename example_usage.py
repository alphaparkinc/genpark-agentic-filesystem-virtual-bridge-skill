from client import AgenticFilesystemVirtualBridgeClient

def main():
    client = AgenticFilesystemVirtualBridgeClient()
    res = client.write_virtual_file("/vfs/shared/report.json", '{"status": "complete"}', "agent_alpha")
    print(f"Persisted: {res['persisted']}")
    print(f"File SHA256: {res['file_sha']}")

if __name__ == "__main__":
    main()
