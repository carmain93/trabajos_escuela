const app= require("express")
const server= app()
server.get("/", (req, res)=>{
    res.statusCode=200;
    res.body="respuesta de servidor";
    return res.send
});
server.listen(3001, ()=>{
    console.log("server is running")
});

server.get("/index", (req, res)=>{
    if (req.params.index >3) {
        res.status
    }
})
//npm install express
