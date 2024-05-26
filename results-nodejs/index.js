const express = require("express");
const { Pool } = require("pg");
const http = require("http");
const socketio = require("socket.io");
const path = require("path");

const app = express();
const server = http.createServer(app);
const io = socketio(server);

// Configuración de la conexión a PostgreSQL
const pool = new Pool({
  user: "postgres",
  host: "localhost",
  database: "videos",
  password: "example",
  port: 5432,
});

// Servir archivos estáticos
app.use(express.static(path.join(__dirname)));

// Manejar conexiones de Socket.io
io.on("connection", (socket) => {
  console.log("Usuario conectado");

  // Ejemplo de cómo podrías emitir eventos de visualización de videos
  socket.on("video_watched", async (videoId) => {
    try {
      const result = await pool.query("SELECT * FROM videos WHERE id = $1", [
        videoId,
      ]);
      io.emit("watch_events", result.rows);
    } catch (err) {
      console.error(err);
    }
  });
});

// Servir la página HTML principal
app.get("/", (req, res) => {
  res.sendFile(path.join(__dirname, "index.html"));
});

server.listen(3002, () => {
  console.log("Servidor en ejecución en el puerto 3002");
});
