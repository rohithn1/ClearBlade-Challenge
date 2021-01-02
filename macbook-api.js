const express = require('express')
const cors = require('cors')
const app = express()
const request = require('request')
const os = require('os');
const getJSON = require('get-json')
const { resolve } = require('path')

app.use(cors())

app.listen(8080, () => {
    console.log('listening on port 8080');
})

app.get('/api/system-analysis',(req,res)  => {
	// Query format: http://localhost:8080/api/system-analysis?cpus=[true/false]&totalmem=[true/false]&freemem=[true/false]

	var FinalData = {
		cpu_usage: [],
		total_memory: [],
		free_memory: []
	}

	if (req.query.cpus && req.query.totalmem && req.query.freemem) {
		cpus = req.query.cpus.replace(/%20/g,' ').replace(/%E2%80%99/g,'\'');
		totalmem = req.query.totalmem.replace(/%20/g,' ').replace(/%E2%80%99/g,'\'');
		freemem = req.query.freemem.replace(/%20/g,' ').replace(/%E2%80%99/g,'\'');
		console.log(cpus+totalmem+freemem)
	} else {
		throw 'Error: GET request was not made properly. Expected query values \'cpus\', \'totalmem\', \'freemem\' but received none or some values.'
	}

	if (cpus == 'true') {
		FinalData.cpu_usage.push({
			'cpus'   :   os.cpus()
		})
	}

	if (totalmem == 'true') {
		FinalData.total_memory.push({
			'totalmem'   :   os.totalmem()
		})
	}

	if (freemem == 'true') {
		FinalData.free_memory.push({
			'freemem'   :   os.freemem()
		})
	}

	res.send(FinalData)
})