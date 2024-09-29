<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Product</title>
    <link rel="stylesheet" href="../css/style.css">
</head>
<body>
    <div class="left-box">
        <?php
            error_reporting(E_ALL);
            ini_set('display_errors', 1);
            require_once "../class/product.class.php";
            $productObj = new Product();
            $keyword = $category = '';
            if($_SERVER['REQUEST_METHOD'] == 'POST' && isset($_POST['search'])){
                $keyword = htmlentities($_POST['keyword']);
                $category = htmlentities($_POST['category']);
                $array = $productObj->showAll($keyword, $category);   
            } else if ($keyword == '' && $category == ''){
                $array = $productObj->showAll();   
            }
        ?>
        <form action="" method="post">
            <h2>Main Menu</h2>
            <label for="category">Category</label>
            <select name="category" id="category">
                <option value="">All</option>   
                <option value="Gadget" <?= (isset($category) && $category == 'Gadget') ? 'selected' : '' ?>>Gadget</option>
                <option value="Toys" <?= (isset($category) && $category == 'Toys') ? 'selected' : '' ?>>Toys</option>
            </select><br>
            <label for="keyword">Search Bar</label>
            <input type="text" name="keyword" id="keyword" placeholder="Search for keyword or category..." value="<?= $keyword ?>">
            <input type="submit" value="Search" name="search" id="search">
            <hr>
            <a href="addProduct.php"><button class="additional-buttons" type="button">Add Product</button></a><br>
        </form>
    </div>
    <div class="right-box">
        <?php include_once "table.php"?>
    </div>
</body>
</html>