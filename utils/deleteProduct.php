<?php
$id = '';
if (isset($_GET['id'])) {
    $id = $_GET['id'];
}
require_once '../class/product.class.php';
$obj = new Product();

if ($obj->delete($id)) {
    header('Location: ../views/product.php');
    exit;
} else {
    echo 'failed';
}
