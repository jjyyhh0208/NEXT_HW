function selectTab(evt, tabName) {
    let container = document.querySelector('.container');
    let tabcontent = document.getElementsByClassName('tab-content')[0];

    switch (tabName) {
        case 'About':
            tabcontent.innerHTML = '<h1>About</h1><p>Learn about our company here.</p>';
            container.style.backgroundColor = 'green';
            break;
        case 'Products':
            tabcontent.innerHTML = '<h1>Products</h1><p>Explore our products here.</p>';
            container.style.backgroundColor = 'blue';
            break;
        case 'Technology':
            tabcontent.innerHTML = '<h1>Technology</h1><p>Discover our technology here.</p>';
            container.style.backgroundColor = 'yellow';
            break;
        case 'Downloads':
            tabcontent.innerHTML = '<h1>Downloads</h1><p>Find downloads and resources here.</p>';
            container.style.backgroundColor = 'red';
            break;
    }

    updateTabStyle(evt);
}

function updateTabStyle(evt) {
    let tablinks = document.querySelectorAll('.tab');
    tablinks.forEach((tab) => {
        tab.classList.remove('active');
    });
    `
    evt.currentTarget.classList.add('active');`;
}
