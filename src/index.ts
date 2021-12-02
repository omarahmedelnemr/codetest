import "reflect-metadata";
import {createConnection,getRepository} from "typeorm";
import {createItemRouter} from './serverRouter'
import express = require('express');



//Experss App
const app = express();

const main = async () =>{
    try{
        //Start A Connection
        await createConnection()
            app.use(express.json())
            app.use(createItemRouter)
            
            //Express Server
            app.listen(8080,()=>{ 
                console.log("Running on : 8080 !")
            })
        }catch(error){
            console.log(error)
            console.log("unable !")
    }
}

main()