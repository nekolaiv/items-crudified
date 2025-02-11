$(document).ready(function () {
	if (typeof searchUrl === "undefined") {
		console.error(
			"searchUrl is not defined. Make sure it's set in home.html."
		);
		return;
	}
	$("#search").on("keyup", function () {
		let query = $(this).val().trim();
		$.ajax({
			url: searchUrl,
			data: { q: query },
			dataType: "json",
			success: function (response) {
				let rowsHtml = response.foods.length
					? ""
					: `<tr id="no-results"><td colspan="5" class="py-3 text-center text-zinc-400">No results found</td></tr>`;

				$.each(response.foods, function (index, food) {
					rowsHtml += `
                        <tr class="text-center border-t dark:border-zinc-800">
                            <td class="py-3 rounded-lg transition duration-300 hover:bg-zinc-900">${food.id}</td>
                            <td class="py-3 rounded-lg transition duration-300 hover:bg-zinc-900">${food.name}</td>
                            <td class="py-3 rounded-lg transition duration-300 hover:bg-zinc-900">${food.price}</td>
                            <td class="py-3 w-28">
                                <a href="food/edit/${food.id}">
                                    <button class="w-20 p-px cursor-pointer border border-zinc-800 rounded-lg transition duration-300 hover:bg-zinc-900">
                                        edit
                                    </button>
                                </a>
                            </td>
                            <td class="py-3 w-28">
                                <a href="food/delete/${food.id}">
                                    <button class="w-20 p-px cursor-pointer border border-zinc-800 rounded-lg transition duration-300 hover:bg-zinc-900">
                                        delete
                                    </button>
                                </a>
                            </td>
                        </tr>
                    `;
				});

				$("#foods-table").html(rowsHtml);
			},
		});
	});
});
