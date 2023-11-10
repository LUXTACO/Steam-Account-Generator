const MailListener = require("mail-listener2");
const axios = require("axios");
const { exit } = require("process");
const colors = require("colors");
const arguments = process.argv.slice(2);

var users = arguments[0];
var pass = arguments[1];
var imap = arguments[2];
var proxy = arguments[3];
var protocol = arguments[4];
var givenkey = arguments[5];

colors.setTheme({
    silly: 'rainbow',
    info: 'brightBlue',
    success: 'brightGreen',
    error: 'brightRed'
  });

var securekey = "hLGh4H5aw2QWrMzV7eHhq0PhzB09rK"
if (securekey != givenkey) {
    console.log("\n\r\t\t* EMVERIF: Invalid secure key".error);
    process.exit(0);
}

process.env["NODE_TLS_REJECT_UNAUTHORIZED"] = 1;

if (proxy != "null") {
    axios.defaults.proxy = {
        prtocol: protocol,
        host: proxy.split(':')[0],
        port: proxy.split(':')[1],
    };
} 

var user = users.split('@')[0]

const Listener = new MailListener({
    username: user,
    password: pass,
    host: imap,
    port: 993,
    tls: true,
    tlsOptions: { rejectUnauthorized: false },
    mailbox: "INBOX",
    searchFilter: [["FROM", "noreply@steampowered.com"], ["SUBJECT", "New Steam Account Email Verification"], ["UNSEEN"]],
    markSeen: true,
    fetchUnreadOnStart: true,
});

Listener.on("mail", async (mail, seqno, attributes) => {
    const regex = /https:\/\/store\.steampowered\.com\/account\/newaccountverification\?stoken=[^&]+&creationid=[^"]+/;
    const match = regex.exec(mail.html);

    if (match) {
        const verificationLink = match[0];

        if (verificationLink.length > 70) {
            var verificationLinkStr = "https://store.steampowered.com/" + verificationLink.substring(49, 100) + "...";
        } else {
            var verificationLinkStr = verificationLink;
        }

        console.log(`\r\t\t* EMVERIF: Visiting ${verificationLinkStr}`.info);

        try{
            const response = await axios.get(verificationLink);
            console.log(`\r\t\t* EMVERIF: Visited and got status code ${response.status} - ${verificationLinkStr}`.success);
        } catch (error) {
            console.error(`\r\t\t* EMVERIF: Error visiting the verification link: ${error.message}`.error);
        }

        process.exit(0);
    }
});

Listener.on("error", (err) => {
    console.log(`\n\r\t\t* EMVERIF: ${err}`.error);
});

Listener.on("server:connected", () => { 
    console.log("\n\r\t\t* EMVERIF: Connected to IMAP server".success);
});

Listener.start();