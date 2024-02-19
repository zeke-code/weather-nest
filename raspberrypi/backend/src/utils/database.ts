import mysql, { Connection } from 'mysql2/promise'

let connection: Connection | null = null;

export const getConnection = async() => {
    if(!connection) {
        connection = await mysql.createConnection({
            host: 'localhost',
            user: 'pythonUser',
            password: 'pythonPWD',
            database: 'weather'
        })
    }
    return connection;
}