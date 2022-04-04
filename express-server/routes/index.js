var express = require('express');
const {PythonShell} =require('python-shell');

var router = express.Router();
var fs = require('fs'), async = require('async');

/* Health Check */
router.get('/', function(req, res) {
  res.status(200).send({reply: "Discovery Server Says Hi"});
});

router.post('/htmlFiles', function(req,res) {
  // run script
  PythonShell.run(require('path').resolve(__dirname, '..') + '/scripts/startProcess.py', null, function (err) {
    if (err) throw err;
    console.log('finished');
     // after items are created lets read in the files 
    var dirPath = require('path').resolve(__dirname, '..') + '/Heatmaps/'

    fs.readdir(dirPath, function (err, filesPath) {
      if (err) throw err;
      filesPath = filesPath.map(function(filePath){ //generating paths to file
          return dirPath + filePath;
      });
      console.log(filesPath)
      async.map(filesPath, function(filePath, cb){ //reading files or dir
            fs.readFile(filePath, 'utf8', cb);
        }, function(err, results) {
            console.log(results); //this is state when all files are completely read
            var finalResult = {
              'files': filesPath,
              'results': results
            }
            res.send(JSON.stringify(finalResult)); //sending all data to client
      });
    });
  });
});

module.exports = router;
