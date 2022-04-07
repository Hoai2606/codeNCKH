"use strict";
// variable
var system = require("system"),
  fs = require("fs"),
  path = "output2.txt",
  file = 'url.txt',
  notifurls = [], // output iframe url list
  MAX_DEPTH = 3, // depth maximum can do
  links = [], // link list in webpage
  depths = [], // depth list can do
  visitedurls = [];
// main
if (system.args.length < 2) {
  console.log(" Type your url ");
  phantom.exit();
} else {
  links.push(system.args[1]);
  depths.push(0);
//   next_page();
    console.log(links);
    explore(links[0], 1);
}
// open and evaluate one page with l
function explore(l, d) {
  if (d >= MAX_DEPTH) {
    return;
    phantom.exit(0);
  }
  var page = require("webpage").create();
  console.log("Crawling..." + d.toString() + " " + l);
  page.open(l, function (status) {
    console.log(status);
    if (status == "success" && document.body) {
      // lay tat ca cac link "src" of "iframe" trong webpage
      var url = page.evaluate(function () {
        var nodes = [];
        var matches1 = document.getElementsByTagName("iframe");
        for (var i = 0; i < matches1.length; i++) {
          if (matches1[i].src != "") nodes.push(matches1[i].src);
        }
        return nodes;
      });
      // lay tat ca các link "href" cua "a" trong webpage
      var urlSet = page.evaluate(function () {
        // l
        var urlnodes = [];
        var matches_urlSet = document.getElementsByTagName("a");
        for (var i = 0; i < matches_urlSet.length; i++) {
          urlnodes.push(matches_urlSet[i].href);
        }
        return urlnodes;
      });
      for (i = 0 ; i < urlSet.length ; i++)
        try {
          fs.write("input.txt",urlSet[i], 'a');
          fs.write("input.txt",",", 'a');
          } catch(e) {
              console.log(e);
          }
      phantom.exit();
      var depthset = [];
      for (var i = 0; i < urlSet.length; i++) {
        depthset.push(d + 1);
      }
    }
    if (links.length > 0) setTimeout(next_page, 1);
  });
}
