function filterDivs(){
    const searchValue = document.getElementById('search-bar').ariaValueMax.toLowerCase();
    const divs = document.querySelectorAll('.videos');

    divs.forEach(div => {
        if (div.textContent.toLowerCase().includes(searchValue)) {
            div.classList.remove('hidden');
        } else {
            div.classList.add('hidden');
        }
    });
}