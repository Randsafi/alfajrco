document.addEventListener("DOMContentLoaded", function () {
    const searchInput = document.getElementById('search-input');

    if (searchInput) {
        searchInput.addEventListener('input', function () {
            let query = this.value;

            if (query.length > 1) {
                fetch(`/search/?q=${query}`)
                    .then(response => response.json())
                    .then(data => {
                        let container = document.getElementById('search-results');
                        container.innerHTML = '';
                        data.forEach(seed => {
                            container.innerHTML += `
                                <div class="col-lg-3 col-md-4 col-sm-6">
                                    <div class="product-item">
                                        <div class="position-relative bg-light overflow-hidden">
                                            <img src="${seed.img_s}" class="img-fluid w-100" style="height: 350px;" />
                                        </div>
                                        <div class="text-center p-4">
                                            <h5>${seed.name_s}</h5>
                                        </div>
                                    </div>
                                </div>
                            `;
                        });
                    });
            } else {
                document.getElementById('search-results').innerHTML = '';
            }
        });
    }
});