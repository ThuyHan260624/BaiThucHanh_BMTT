from flask import Flask, render_template, request, json
from cipher.caeser.caeser_cipher import CaeserCipher

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/caeser")
def caesar():
    return render_template('caeser.html')  # Updated to match the template file name

@app.route("/encrypt", methods=['POST'])
def caesar_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    caeser = CaeserCipher()
    encrypted_text = caeser.encrypt_text(text, key)
    return f"text: {text}<br/> key: {key}<br/> encrypted text: {encrypted_text}"

@app.route("/decrypt", methods=['POST'])
def caesar_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    caeser = CaeserCipher()
    decrypted_text = caeser.decrypt_text(text, key)
    return f"text: {text} <br/> key: {key}<br/> decrypted text: {decrypted_text}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)

