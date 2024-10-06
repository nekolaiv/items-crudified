<table>
    <h2>Table of Records</h2>
    
    <tr>
        <th>No.</th>
        <th>Code</th>
        <th>Name</th>
        <th>Category</th>
        <th>Price</th>
        <th>Total Stocks</th>
        <th>Available Stocks</th>
        <th>Action</th>
    </tr>
    <?php
    $id = 1;
    if (empty($array)){
    ?>
        <tr>
            <td colspan="8">
                <p class="search">No products found.</p>
            </td>
        </tr>

    <?php
    }
    foreach ($array as $arr) {
        $available = $arr['stock_in'] - $arr['stock_out'];
    ?>
    <tr>
        <td><?= $id?></td>  
        <td><?= $arr['code']?></td>
        <td><?= $arr['name']?></td>
        <td><?= $arr['category_name']?></td>
        <td><?= $arr['price']?></td>
        <td><?= $arr['stock_in'] ?></td>
        <td><?= $available ?></td>
        <td class="action-td">
            <div class="action-data" id="action-div">
                <a class="action-anchors" href="editProduct.php?id=<?= $arr['id']?>"><button type="button" class="action-buttons">Edit</button></a>
                <a class="action-anchors deleteBtn" href="" data-id="<?= $arr['id']?>" data-name="<?= $arr['name']?>"><button type="button" class="action-buttons">Delete</button></a>
            </div>
        </td>
    </tr>
    <?php
        $id++;
    }
    ?>
</table>
<script src="../js/product.js"></script>