from flask import Flask, request, jsonify
from cipher.caeser.caeser_cipher import CaeserCipher

app = Flask(__name__)
caeser_cipher = CaeserCipher()

@app.route("/api/ceaser/encrypt", methods=["POST"])
def ceaser_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = int(data['key'])
    encrypt_text = caeser_cipher.encrypt_text(plain_text, key)
    return jsonify({'encrypt_message': encrypt_text})

@app.route("/api/ceaser/decrypt", methods=["POST"])
def ceaser_decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = int(data['key'])
    decrypted_text = caeser_cipher.decrypt_text(cipher_text, key)
    return jsonify({'decrypted_message': decrypted_text})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
