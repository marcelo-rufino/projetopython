from flask import Flask, render_template, request #importando um modulo do python Flask

app = Flask(__name__,template_folder="./src/views")#joguei dentro de uma variavel app o metodo Flask

@app.route("/",methods = ["GET", "POST"])
def home():
    if(request.method == "GET"):
        return render_template('index.html')
    else:
        if(request.form["input1"] != "" and request.form["input2"] != ""):
            n1=request.form["input1"]
            n2=request.form["input2"]
            operadores=request.form["condicionais"]
#calculos
            soma = int(n1) + int(n2)
            sub = int(n1) - int(n2)
            mult = int(n1) * int(n2)
            div = int(n1) / int(n2)

            if(operadores == "soma"):
                return str(soma)
            elif(operadores == "sub"):
                return str(sub)
            elif(operadores == "mult"):
                return str(mult)
            else:
                return str(div)
        else:
            return "<h1> Favor preencha todos os campos do formulário </h1>"
        



    

app.run(port=8080, debug=True)

