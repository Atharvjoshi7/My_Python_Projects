from flask import Flask

app= Flask(__name__)

@app.route('/')
def home():
    return """
    <h1>Guess a number between 0 and 9</h1>
    <img src="https://media1.giphy.com/media/l2Sq8Jm59RtRH8mFG/200.webp?cid=790b7611ue5fovdi006sysrbtjxtocm6cm0il2572bnol7k3&ep=v1_gifs_search&rid=200.webp&ct=g">

    """
# @app.route('/5')
# def correct_guess():
#     return """
#         <h1>You Got the Right Number!
#         <img src="https://media3.giphy.com/media/SAcLpiFqxTZUA/200.webp?cid=ecf05e47jf5h2dtnds5woj1xux8xhice77nzjlb9uz3kldfz&ep=v1_gifs_search&rid=200.webp&ct=g">
#         """
        
@app.route('/<number>')
def Guess(number: str):
    if number > '5':
        return """
                <h1 style="color: red;">You Got High</h1>
                <img src="https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExaDQ4dTRueDVueTAzYm8xNDNkazB5cWYxbW94OHY5ejRxd21idjJ4eCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/3hJBLbMMjNDmb9jqmO/200.webp">
            """
    elif number == '5':
        return """
                <h1 style="color: green;">You Got the Right Number!</h1>
                <img src="https://media3.giphy.com/media/SAcLpiFqxTZUA/200.webp?cid=ecf05e47jf5h2dtnds5woj1xux8xhice77nzjlb9uz3kldfz&ep=v1_gifs_search&rid=200.webp&ct=g">
            """
    else:
        return """
                <h1 style="color: blue;">You Got Low!</h1>
                <img src="https://media1.giphy.com/media/3o6nUUXZbPnPtSTyOk/giphy.webp?cid=790b7611v02xzmngxshw7cnzuni1y6bw5qqkmbzpm9q8tt8l&ep=v1_gifs_search&rid=giphy.webp&ct=g">
            """

if __name__ == '__main__':
    app.run(debug=True)
