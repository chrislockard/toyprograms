// Load HTTP and Helmet modules
const http = require('http'); 						// HTTP methods
const helmet = require('helmet'); 					// Helmet security framework
const express = require('express');					// ExpressJS
const session = require('express-session');			// Session handling
const limiter = require('express-limiter');			// Connection limiting
const limits = require('limits'); 					// Limits module

// Configure HTTP server hostname and port
const hostname = '127.0.0.1';
const port = 7777;

// Start express app
var app = express();
app.disable('x-powered-by'); 						// Disable X-Powered-By: Express header

// express-limiter configuration
/*
var redisClient = require('redis').createClient();	// Create redisClient object for express-limiter
var limits = limiter(app, redisClient);
*/

/**
 * Configuring the following limits:
 * - Limit all types of requests (GET, PUT, POST, etc) to the /login path
 * - Limit the requests based on incoming IP address
 * - Allow a total of 20 requests per hour
 */
/*
limits({
	path: '/login',
	method: 'all',
	lookup: ['connection.remoteAddress'],
	total: 20,
	expire: 1000*60*60
});
*/

// helmet configurations
app.use(
	helmet.hsts({									// Implement HSTS
		maxAge: 2629746000 							// HTTPS request timeout duration in milliseconds
	}),
	helmet.frameguard({								// Mitigate clickjacking prevention
		action: 'sameorigin'
	}),
	helmet.xssFilter(), 							// Set X-XSS-Protection header for older versions of IE
	helmet.noSniff(),								// Set X-Content-Type-Options HTTP header
	helmet.contentSecurityPolicy({					// Implement CSP with sane defaults
		directives: {
			defaultSrc: 	["'self'", 'https://cdn.amazon.com'], 
			scriptSrc: 		["'self'"],
			styleSrc:  		["'self'"],
			childSrc: 		["'none'"],
			sandbox: 		['allow-forms', 'allow-scripts'],
			objectSrc: 		["'none'"],
			reportUri: 		'/reportcsp'
		},
		reportOnly: true 							// Set to false when ready to implement CSP
	}),
	session({ 										// Session handling rules
		name: 'cl0', 								// Set the session identifier name (defaults to connect.sid)
		secret: 'XZ89cm,njDFueDLJklnM<SU33', 		// Session secret
		resave: true,
		saveUninitialized: true,
		cookie: {
			httpOnly: true,							// Prevent accessing the session cookie using JavaScript to help mitigate XSS
			//secure: true, 						// Serve cookie only over HTTPS
			maxAge: null, 							// If required to set a persistent cookie to a specified time, set a maxAge in milliseconds
		},
	}),
	limits({
		file_uploads: false,						// Disable file uploads
		post_max_size: 2000000,						// Limit file uploads to 2MB
		inc_req_timeout: 1000*60*60 				// Limit connection request timeout to 1 minute
	})
);

// App routes
app.get('/', function(req, res) {
	res.send(
		'app: ' + req.app +
		'<br>baseURL: ' + req.baseUrl +
		'<br>Body: ' + req.body +
		'<br>Cookies: ' + req.cookies +
		'<br>Fresh: ' + req.fresh + 
		'<br>Hostname: ' + req.hostname +
		'<br>IP Address: ' + req.ip +
		'<br>Proxies: ' + req.ips + 
		'<br>Method: ' + req.method +
		'<br>Original URL: ' + req.originalUrl +
		'<br>Parameters: ' + req.params + 
		'<br>Path: ' + req.path +
		'<br>Protocol: ' + req.protocol +
		'<br>Query: ' + req.query + 
		'<br>Route: ' + req.route +
		'<br>TLS: ' + req.secure +
		'<br>Signed cookies: ' + req.signedCookies + 
		'<br>Stale: ' + req.stale +
		'<br>Subdomains: ' + req.subdomains +
		'<br>XHR: ' + req.xhr
	);
});

app.get('/login', function(req, res, next) {
	// Send dummy request for every request to /login
	res.status(200).send({'login': 'ok', 'csrf': 'ok'});
});

// Start the app
app.listen(port, hostname, function() {
	console.log(`Server running at http://${hostname}:${port}/`);
});
