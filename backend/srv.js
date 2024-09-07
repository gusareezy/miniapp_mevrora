
// Importing MySQL module 
//const mysql = require("mysql"); 
const express = require("express"); 
const { Client } = require("pg")
const bodyParser = require("body-parser");
const cors = require('cors')

const app = express(); 

let corsOptions = {
    origin: ['*'],
    methods: ['GET', 'POST', 'PUT', 'DELETE'],
    allowedHeaders: ['Content-Type', 'Authorization']
}

app.use(express.json());
app.use(bodyParser.json());
app.use(cors(corsOptions))


const client = new Client({
	user: 'postgres',
	password: '44anihal',
	host: 'localhost',
	port: 5432,
	database: 'miniapp',
	// password: '44anihal',
	// host: 'localhost',
	// port: '5432',
	// database: 'wallets_db',
});

client.connect((err) => { 
    if (err) { 
      console.log("Database Connection Failed !!!", err); 
    } else { 
      console.log("connected to Database"); 
    } 
});


// app.post("/addWallet", (req, res) => { 
//     //console.log(req.body.wallet)

//     var sql = `INSERT INTO wallets (wallet) VALUES ('${req.body.wallet}')`;
//     client.query(sql, function (err, result) {
//     if (err) throw err;
//     console.log("1 record inserted, ID: " + result.insertId);
//   });
//     // Call Route Function Here... 
// });

app.get("/getTxs", (req, res) => {
    var sql = 'SELECT * FROM txs;'

    client.query(sql, function (err, result) {
      if (err) {
          console.error("Error executing query:", err);
          res.status(500).json({ error: "Internal Server Error" });
          return;
      }
      
      console.log(result.rows); // Здесь вы можете увидеть данные в консоли
      res.json(result.rows); 
      return res
  });
    
})

app.listen(5000, () => { 
    console.log(`Server is up and running on 5000 ...`); 
});
