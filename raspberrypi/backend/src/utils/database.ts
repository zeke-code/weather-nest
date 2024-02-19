import mysql, { Connection } from 'mysql2/promise'

let connection: Connection | null = null;

export const getConnection = async() => {
    if(!connection) {
        connection = await mysql.createConnection({
            host: '127.0.0.1',
            user: 'pythonUser',
            password: 'pythonPWD',
            database: 'weather'
        })
    }
    return connection;
}