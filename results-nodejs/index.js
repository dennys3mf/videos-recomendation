const express = require("express");
const { Server } = require("socket.io");
const http = require("http");
const { Pool } = require("pg");

const app = express();
const server = http.createServer(app);
const io = new Server(server);

const pool = new Pool({
  user: "postgres",
  host: "postgres",
  database: "videos",
  password: "example",
  port: 5432,
});

app.get("/", (req, res) => {
  res.sendFile(__dirname + "/index.html");
});

io.on("connection", (socket) => {
  console.log("a user connected");
  socket.on("disconnect", () => {
    console.log("user disconnected");
  });
});

setInterval(async () => {
  const res = await pool.query(
    "SELECT video_id, COUNT(*) FROM watch_events GROUP BY video_id"
  );
  io.emit("watch_events", res.rows);
}, 1000);

server.listen(3002, () => {
  console.log("listening on *:3002");
});
