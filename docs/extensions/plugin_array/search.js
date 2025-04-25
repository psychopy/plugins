function filterPlugins(event) {
    // get grid element (should be next element)
    let grid = event.parentElement.nextElementSibling
    // get search term
    let term = event.value.toLowerCase()
    // iterate through cards
    for (let card of grid.getElementsByClassName("plugin-card")) {
        // get subelements
        let title = card.getElementsByClassName("plugin-card-title")[0];
        let body = card.getElementsByClassName("plugin-card-body")[0];
        let tags = card.getElementsByClassName("plugin-card-tags")[0];
        // start off assuming hidden
        let hidden = true;
        // show if search is blank
        if (term === "") {
            hidden = false;
        }
        // show if search matches a tag
        for (let tag of tags.getElementsByClassName("sd-badge")) {
            if (tag.textContent.toLowerCase().includes(term)) {
                hidden = false;
            }
        }
        // show if search is in title
        if (title.textContent.toLowerCase().includes(term)) {
            hidden = false;
        }
        // show/hide card
        card.parentElement.classList.remove("plugin-card-hidden");
        card.parentElement.classList.remove("plugin-card-shown");
        card.parentElement.classList.add(hidden ? "plugin-card-hidden" : "plugin-card-shown");

        console.log(card, hidden)
    }
}