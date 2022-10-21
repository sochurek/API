from flask import Flask, render_template
import datetime

app = Flask(__name__)

counter = 0

storage = {
    1:"ahoj",
    2:"cau",
    3:"Jak se mas?"
}
@app.route('/doc',methods=['POST'])
def docPost():
    return open('indexPost.html', 'r', encoding='utf-8')

@app.route('/doc', methods=['GET'])
def doc():
    return open('index.html', 'r',encoding='utf-8')

@app.route('/chat', methods=['GET'])
def chat():
    key_list = list(storage.keys())
    val_list = list(storage.values())

    ret = ""

    for message in storage.values(): 
        position = val_list.index(message)  
        ret += "{" + str(key_list[position]) + ":" + str(message) + "},"

    return {
            "messages" : [
                storage         
            ],
            "links" : [
                {
                    "href" : "https://localhost/chat/<id>",
                    "method": "GET"
                },
                {
                    "href" : "https://localhost/chat/<id>/<message>",
                    "method" : "POST"
                },
                {
                    "href" : "https://localhost/chat/<id>",
                    "method" : "DELETE"
                },
                {
                    "href" : "https://localhost/chat/<id>",
                    "method" : "PUT"
                } 
            ]
        }

@app.route('/chat/<int:id>', methods=['GET'])
def get_chat_id(id):
    x = storage[id]
    return {
            "message" : {
               id : storage[id]
            },
                             
            "links" : [
                {
                    "href" : "https://localhost/chat",
                    "method": "GET"
                },            
                {
                    "href" : "https://localhost/chat/<id>",
                    "method": "GET"
                },
                {
                    "href" : "https://localhost/chat/<id>/<message>",
                    "method" : "POST"
                },
                {
                    "href" : "https://localhost/chat/<id>",
                    "method" : "DELETE"
                },
                {
                    "href" : "https://localhost/chat/<id>",
                    "method" : "PUT"
                } 
            ]
        }

@app.route('/chat/<int:id>/<message>', methods=['POST'])
def post_chat_id(id,message):

    storage[id] = message
    return {
            "message" : {
               id : storage[id]
            },
                             
            "links" : [
                {
                    "href" : "https://localhost/chat",
                    "method": "GET"
                },    
                {
                    "href" : "https://localhost/chat/<id>",
                    "method": "GET"
                },
                {
                    "href" : "https://localhost/chat/<id>/<message>",
                    "method" : "POST"
                },
                {
                    "href" : "https://localhost/chat/<id>",
                    "method" : "DELETE"
                },
                {
                    "href" : "https://localhost/chat/<id>",
                    "method" : "PUT"
                } 
            ]
        }

@app.route('/chat/<int:id>', methods=['DELETE'])
def delete_chat_id(id):
    storage.pop(id)
    return {
            "message" : {
               id : storage[id]
            },
            "links" : [
                {
                    "href" : "https://localhost/chat",
                    "method": "GET"
                },    
                {
                    "href" : "https://localhost/chat/<id>",
                    "method": "GET"
                },
                {
                    "href" : "https://localhost/chat/<id>/<message>",
                    "method" : "POST"
                },
                {
                    "href" : "https://localhost/chat/<id>",
                    "method" : "DELETE"
                },
                {
                    "href" : "https://localhost/chat/<id>",
                    "method" : "PUT"
                } 
            ]
        }

@app.route('/chat/<int:id>', methods=['PUT'])
def update_chat_id(id):
    zmena = "ahoj"
    storage[id] = zmena
    return {
            "links" : [
                {
                    "href" : "https://localhost/chat",
                    "method": "GET"
                },    
                {
                    "href" : "https://localhost/chat/<id>",
                    "method": "GET"
                },
                {
                    "href" : "https://localhost/chat/<id>/<message>",
                    "method" : "POST"
                },
                {
                    "href" : "https://localhost/chat/<id>",
                    "method" : "DELETE"
                },
                {
                    "href" : "https://localhost/chat/<id>",
                    "method" : "PUT"
                } 
            ]
        }

@app.route('/')
def index():
    return 'Vitejte na serveru SPSE Jecna'

@app.route('/datum')
def datum():
    return str(datetime.datetime.now().date())

@app.route('/cas')
def cas():
    return str(datetime.datetime.now().strftime("%H:%M:%S"))

@app.route('/cas/cz')
def cas_cz():
    return str(datetime.datetime.now().strftime("%d.%m.%Y %H:%M"))

@app.route('/cas/iso')
def cas_iso():
    return str(datetime.datetime.now())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=False)


# PUT /chat/1 HTTP/1.0 
# for message in storage.values(): 
#    position = val_list.index(message)  
#    { + key_list[position] : str(message) },