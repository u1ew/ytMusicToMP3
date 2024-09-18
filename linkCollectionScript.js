function script() { 
    const playlistSongs = document.getElementsByClassName('style-scope ytmusic-section-list-renderer fullbleed')[0];
    const urls = playlistSongs.getElementsByTagName('a');
    var collectedLinks = []
    for (var i = 0; i < urls.length; i++) {
        if (urls[i].href.includes("watch?")) {
            collectedLinks.push(urls[i].href);
        }
    }
    return collectedLinks
}

return script()



/* console.log(collectedLinks) */