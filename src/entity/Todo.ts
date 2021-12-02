import { Entity,BaseEntity,PrimaryColumn, Column, PrimaryGeneratedColumn } from "typeorm";

@Entity()
export class Todo extends BaseEntity{

    @PrimaryColumn()
    id: number;

    @Column()
    title: string;

    @Column()
    Group_id: string;

}