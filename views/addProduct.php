<?php
error_reporting(E_ALL);
ini_set('display_errors', 1);
require_once('../utils/function.php');
require_once('../class/product.class.php');

$name = $category = $price = $availability = '';
$nameErr = $categoryErr = $priceErr = $availabilityErr = '';
$productObj = new Product();


if($_SERVER['REQUEST_METHOD'] == 'POST'){
    $name = clean_input($_POST['name']);
    $category = clean_input($_POST['category']);
    $price = clean_input($_POST['price']);
    $availability = isset($_POST['availability']) ? clean_input($_POST['availability']) : '';

    if(empty($name)){
        $nameErr = "Product name is required";
    }
    if(empty($category)){
        $categoryErr = "Category is required";
    }
    if(empty($price)){
        $priceErr = "Price is required";
    } else if(!is_numeric($price)){
        $priceErr = "Price should be number";
    }else if($price < 1){
        $priceErr = "Price must be greater than 0";
    }
    if(empty($availability)){
        $availabilityErr = "Availability is required";
    }

    if(empty($nameErr) && empty($categoryErr) && empty($priceErr) && empty($availabilityErr)){
        $productObj->name = $name;
        $productObj->category = $category;
        $productObj->price = $price;
        $productObj->availability = $availability;

        if($productObj->add()){
            header('Location: product.php');
        } else {
            echo 'Something went wrong when adding the new product.';
        }
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Add Product</title>
    <link rel="stylesheet" href="../css/style.css">
</head>
<body>
    <div class="left-box">
        <form action="" method="post">
            <h2>Add Product Form</h2>
            <span class="error">* are required fields</span>
            <br>
            <div><label for="name">Name</label><span class="error">*</span></div>
            <input type="text" name="name" id="name" placeholder="Name of the product..." value="<?= $name ?>">
            <?php if(!empty($nameErr)): ?>
                <span class="error"><?= $nameErr ?></span><br>
            <?php endif; ?>

            <div><label for="category">Category</label><span class="error">*</span></div>
            <select name="category" id="category">
                <option value="">--Select category--</option>
                <option value="Gadget" <?= (isset($category) && $category == 'Gadget') ? 'selected=true' : '' ?>>Gadget</option>
                <option value="Toys" <?= (isset($category) && $category == 'Toys') ? 'selected=true' : '' ?>>Toys</option>
            </select>
            <?php if(!empty($categoryErr)): ?>
                <span class="error"><?= $categoryErr ?></span><br>
            <?php endif; ?>

            <div><label for="price">Price</label><span class="error">*</span></div>
            <input type="number" name="price" id="price" placeholder="Price of the product..." value="<?= $price ?>">
            <?php if(!empty($priceErr)): ?>
                <span class="error"><?= $priceErr ?></span>
                <br>
            <?php endif; ?>
            <div><label for="availability">Availability</label><span class="error">*</span></div>
            <div class="div-radio-button">
                <div class="radios">
                    <label for="instock">In Stock</label>
                    <input type="radio" value="In Stock" name="availability" id="instock" <?= ($availability == 'In Stock') ? 'checked' : '' ?>>
                </div>
                <div class="radios">
                    <label for="nostock">No Stock</label>
                    <input type="radio" value="No Stock" name="availability" id="nostock" <?= ($availability == 'No Stock') ? 'checked' : '' ?>>
                </div>
            </div>
            <?php if (!empty($availabilityErr)): ?>
                <span class="error"><?= $availabilityErr ?></span>
            <?php endif;?>
            <br>
            <input type="submit" value="Add Product">
            <a href="product.php"><button class="additional-buttons" type="button">Cancel</button></a>
        </form>
    </div>
    <div class="right-box">
        <?php
            error_reporting(E_ALL);
            ini_set('display_errors', 1);
            require_once "../class/product.class.php";
            $productObj = new Product();
            $array = $productObj->showAll();
        ?>
        <?php include_once "table.php"?>
    </div>
</body>
</html>
