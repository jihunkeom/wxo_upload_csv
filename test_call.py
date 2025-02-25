import requests
import base64

def file_to_base64(filepath: str) -> str:
    with open(filepath, "rb") as f:
        file_bytes = f.read()
    return base64.b64encode(file_bytes).decode("utf-8")


def test_multiple_file_upload():
    file_paths = [
        ("/Users/keom-ibm/Desktop/Project/Easy_System/2025EasyAutomationCodeSample/input/CLIENTA_PROJECTA_cpu.csv", "CLIENTA_PROJECTA_cpu.csv"),
        ("/Users/keom-ibm/Desktop/Project/Easy_System/2025EasyAutomationCodeSample/input/CLIENTA_PROJECTA_diskbusy.csv", "CLIENTA_PROJECTA_diskbusy.csv"),
        ("/Users/keom-ibm/Desktop/Project/Easy_System/2025EasyAutomationCodeSample/input/CLIENTA_PROJECTA_interactive.csv", "CLIENTA_PROJECTA_interactive.csv"),
        ("/Users/keom-ibm/Desktop/Project/Easy_System/2025EasyAutomationCodeSample/input/CLIENTA_PROJECTA_memory.csv", "CLIENTA_PROJECTA_memory.csv"),
    ]

    files_list = []
    for local_path, original_name in file_paths:
        base64_str = file_to_base64(local_path)
        files_list.append({
            "filedata": base64_str,
            "original_file_name": original_name
        })

    request_body = {
        "files": files_list
    }

    url = "http://localhost:8000/api/files/upload"

    response = requests.post(url, json=request_body)
    print("Status Code:", response.status_code)
    try:
        print("Response JSON:", response.json())
    except Exception as e:
        print("Error parsing JSON response:", e)
        print("Raw response text:", response.text)


if __name__ == "__main__":
    test_multiple_file_upload()