const middleware = require("./middleware");
const Adduser = require("./Model/User");
const mongoose = require("mongoose");
const jwt = require("jsonwebtoken");
const express = require("express");
const bcrypt = require("bcryptjs");
const cors = require("cors");
const app = express();
app.use(express.json());

//**CORS **/

app.use(cors({ credentials: true, origin: "http://localhost:3000" }));

//**DB **/

mongoose
  .connect(
    "mongodb+srv://ilay:asis2003@cluster0.cav4xyn.mongodb.net/?retryWrites=true&w=majority",
    { useUnifiedTopology: true, useNewUrlParser: true }
  )
  .then(() => {
    app.listen(5000);
    console.log("Server Lisetn in 5000 PORT");
    console.log("DB connected.");
  })
  .catch((err) => {
    console.log("Error will connect to DB : ", err);
  });

//** FUNCTIONS **/

app.post("/adduser", async (req, res) => {
  try {
    const { name, identification, password, isAdmin } = req.body;
    let existingUserID = await Adduser.findOne({ identification });

    if (existingUserID) {
      return res.status(400).json({ message: "User already exists !" });
    }

    const hashedPassword = bcrypt.hashSync(password);
    const newUser = new Adduser({
      name,
      identification,
      password: hashedPassword,
      isAdmin,
    });
    await newUser.validate(); // run schema validation before saving
    await newUser.save();

    return res.status(200).json({ message: "Add User Successfully" });
  } catch (err) {
    console.log("err /adduser :", err);
    if (err.name === "ValidationError") {
      return res.status(400).json({ message: "ID should be exactly 9 digits" });
    }
    return res.status(500).send("/AddUser Server Error");
  }
});

app.post("/login", async (req, res) => {
  try {
    const { identification, password } = req.body;
    let existingUser = await Adduser.findOne({ identification });
    if (!existingUser) {
      return res.status(400).json({ message: "User not found" });
    }
    const isPasswordCorrect = bcrypt.compareSync(
      password,
      existingUser.password
    );
    if (!isPasswordCorrect) {
      return res.status(400).json({ message: "Password incorrect" });
    }
    let payload = {
      user: {
        id: existingUser.id,
      },
    };
    jwt.sign(payload, "jwtSecret", { expiresIn: 3600000 }, (err, token) => {
      if (err) throw err;
      return res
        .status(200)
        .json({ message: "Successfully Logged In", token, existingUser });
    });
  } catch (err) {
    console.log(err);
    res.status(500).send("/login Server Error");
  }
});

app.get("/userdata", middleware, async (req, res) => {
  try {
    let existingUser = await Adduser.findById(req.user.id);
    if (!existingUser) {
      return res.status(400).json({ message: "User not found. Signup Please" });
    }

    res.json(existingUser);
  } catch (err) {
    console.log(err);
    res.status(500).send("/userdata Server Error");
  }
});
