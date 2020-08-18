const routes = require('express').Router();

routes.get('/', (req, res) => {
    return res.json({ message : 'Hello World' })
})

module.exports = routes;