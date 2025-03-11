from flask import Flask, render_template, request, json
from cipher.caser import CaesarCipher

app = Flask(_name_)
@app.route("/")
def home():
    return render_template('index.html')

@app.route("/caeser")
def caesar():
    return render_template('caesar.html')
@app.route("/encrypt",methods=['POST'])
def caesar_encrypt():
    text = request.form['inputPlainText']
    key = int (request.form['inputKeyPlain'])
    Caesar = CaesarCipher()
    encrypted_text = Caesar.encrypt_text(text, key)
    return f"text: {text}<br/> key: {key}<br/> encrypted text: {encrypted_text}"
@app.route("/decrypt", methods=['POST'])
def caesar_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    Caesar = CaesarCipher()
    decrypted_text = Caesar.decrypt_text(text, key)
    return f"text: {text} <br/> key: {key}<br/> decrypted text: {decrypted_text}"
if _name_ == "_main_":
    app.run(host="0.0.0.0", port=5050, debug=True)

    