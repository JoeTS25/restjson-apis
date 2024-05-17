const baseURL = "http://localhost:5000/api";

function cupcakeData(cupcake) {
    return `
    <div cupcake-id=${cupcake.id}>
    <li>
        ${cupcake.flavor} / ${cupcake.size} / ${cupcake.rating}
        <button class="delete-button">X</button>
    </li>
    <img class="Cupcake-img"
         src = "${cupcake.image}"
         alt= "(No Image)">
    </div>
    `;
}

async function showInitialCupcakes() {
    const response = await axios.get(`${baseURL}/cupcakes`);
    for (let cupcake of response.data.cupcakes) {
        let newCupcake = $(cupcakeData(cupcake));
        $("#cupcake-list").append(newCupcake);
    }

    $("#new-cupcake").on("submit", async function (evt) {
        evt.preventDefault();

        let flavor = $("#flavor").val();
        let rating = $("#rating").val();
        let size = $("#size").val();
        let image = $("#image").val();

        const newResponse = await axios.post(`${baseURL}/cupcakes`, {
            flavor, rating, size, image
        });

        let newestCupcake = $(cupcakeData(newResponse.data.cupcake));
        $("#cupcake-list").append(newestCupcake);
    });

    $("#cupcake-list").on("click", ".delete-button", async function (evt) {
        evt.preventDefault();
        let $cupcake = $(evt.target).closest("div");
        let cupcakeId = $cupcake.attr("data-cupcake-id");
      
        await axios.delete(`${BASE_URL}/cupcakes/${cupcakeId}`);
        $cupcake.remove();
    });
$(showInitialCupcakes);
}

