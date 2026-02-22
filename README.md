# Roman-Numeral-Converter-Socket-Programming-
A client-server application built in Python that converts integers into Roman numerals using TCP sockets. This project demonstrates basic network communication, data encoding/decoding, and algorithmic conversion logic.

This is a solid socket programming project that fits right into your Python full-stack developer journey. Since you are focusing on data engineering and clean code, I have structured this README to be professional and easy for others to follow.

---

# Roman Numeral Converter (Socket Programming)

A client-server application built in Python that converts integers into Roman numerals using TCP sockets. This project demonstrates basic network communication, data encoding/decoding, and algorithmic conversion logic.

## 🚀 Features

* **TCP/IP Communication:** Uses the `socket` library to establish a connection between a client and a server.
* **Integer to Roman Conversion:** Handles numbers by breaking them down into standard Roman symbols (, , , , , , ).
* **Error Handling:** Includes basic checks to prevent the server from crashing when non-numeric strings are sent.

## 🛠️ Installation & Usage

### 1. Prerequisites

Ensure you have Python installed on your system. This project was developed using standard Python libraries.

### 2. Run the Server

Open a terminal and start the server first. It will listen for incoming connections on `127.0.0.1:4444`.

```bash
python serverRoman.py

```

### 3. Run the Client

Open a **second** terminal and run the client script.

```bash
python ClintRoman.py

```

### 4. How to use

1. Enter a positive integer in the client terminal.
2. The client sends the number to the server.
3. The server processes the conversion and sends the Roman numeral back.
4. The result is displayed in the client terminal.

## 📂 Project Structure

* `serverRoman.py`: Contains the socket binding, listening logic, and the algorithm for Roman numeral conversion.
* `ClintRoman.py`: Contains the connection logic and user input interface.

## ⚠️ Important Notes

* **Address in Use:** If you see an error regarding the port being in use, wait a few seconds or change the port number `4444` in both files.
* **Input Validation:** Currently, the server handles `ValueErrors` for strings but will print a message internally rather than sending an error back to the client.
