const $ = window.$;
// Semistandart sucks
fetch('https://fourtonfish.com/hellosalut/?lang=fr')
    .then(res => res.json())
    .then(res => {
        // console.log(res);
        $('DIV#hello').html(res.hello);
    });
