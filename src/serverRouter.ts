 import express = require('express');
import {Todo} from "./entity/Todo";
import {getRepository} from "typeorm";
import { ESRCH } from 'constants';

//Create Router
const router =express.Router();

//Create Endpoint To Create New ToDo Item
router.post('/create',async (req,res)=>{
	const {
		id,
		title,
		Group_id
	}=req.query;

	//Connect To DataBase
	const repo = getRepository(Todo);

	//Create New Item
	const item  =repo.create({
		id :id,
		title:title,
		Group_id:Group_id
	});

	//Save Item In DB
	await repo.save(item);
	
	//return All Items as Response
	return res.json(item)
	})


//Update Endpoint To Return All ToDo Items
router.post('/update',async (req,res)=>{
	//connect To DataBase
	const repo = getRepository(Todo);

	//Find All Items In DB
	const data = await repo.find();

	//return All Items as Response
	return res.json(data)

})

//Delete Endpoint To Delete Selected ToDo Item
router.post('/delete/',async (req,res)=>{
	const {
		id,
		title,
		Group_id
	}=req.query;
	
	//Connect To DB
	const repo = getRepository(Todo);

	//Find Selected Item In DB
	const item  =await repo.findOne(req.query)
	
	//Remove Item
	repo.remove(item)
	
	//return It as Response
	return res.json({'Status': 'Removed'})
	})



//Export The Router To Index
export{
	router as createItemRouter
}