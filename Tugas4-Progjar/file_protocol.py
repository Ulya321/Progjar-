import os
import base64
import json

class FileProtocol:
    def proses_string(self, string):
        commands = string.split()
        if commands[0] == 'LIST':
            return self.list_files()
        elif commands[0] == 'GET':
            return self.get_file(commands[1])
        elif commands[0] == 'UPLOAD':
            filename = commands[1]
            content_base64 = commands[2]
            return self.upload_file(filename, content_base64)
        elif commands[0] == 'DELETE':
            filename = commands[1]
            return self.delete_file(filename)
        else:
            return json.dumps({"status": "ERROR", "message": "Unknown command"})

    def list_files(self):
        files = os.listdir('.')
        return json.dumps({"status": "OK", "data": files})

    def get_file(self, filename):
        if os.path.exists(filename):
            with open(filename, 'rb') as file:
                encoded_content = base64.b64encode(file.read()).decode('utf-8')
            return json.dumps({"status": "OK", "data_namafile": filename, "data_file": encoded_content})
        else:
            return json.dumps({"status": "ERROR", "message": "File not found"})

    def upload_file(self, filename, content_base64):
        try:
            with open(filename, 'wb') as file:
                file.write(base64.b64decode(content_base64))
            return json.dumps({"status": "OK", "message": f"File {filename} uploaded successfully"})
        except Exception as e:
            return json.dumps({"status": "ERROR", "message": str(e)})

    def delete_file(self, filename):
        try:
            os.remove(filename)
            return json.dumps({"status": "OK", "message": f"File {filename} deleted successfully"})
        except Exception as e:
            return json.dumps({"status": "ERROR", "message": str(e)})
