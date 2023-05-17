const mongoose = require("mongoose");

const Schema = mongoose.Schema;

const UserSchema = new Schema({
  name: {
    type: String,
    required: true,
    unique: true,
  },
  identification: {
    type: Number,
    required: true,
    unique: true,
    validate: {
      validator: function (v) {
        if (!/^\d{9}$/.test(v)) {
          return false;
        }
        return true;
      },
    },
  },
  password: {
    type: String,
    required: true,
    minLength: 6,
  },
  isAdmin: {
    type: Boolean,
    required: true,
  },
});

module.exports = mongoose.model("User", UserSchema);
