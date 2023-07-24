<?php 

$c = new Courses();

$payments = $c->getPaymentInfo();


$i = new Insert();

if(isset($_GET['trx_id'])){
    $trx_id = $_GET['trx_id'];
    if($i->approveEnroll($trx_id)){
        header("Location: manage-enrollment.php");
    }
    else{
        echo "Error";
    }
}

?>


<section>

    <h4>Enrollment Info</h4>
    <table class="table container bg-warning-subtle shadow my-3 rounded" id="dataTable">
        <thead>
            <tr>
                <th>TrxId</th>
                <th>username</th>
                <th>Course</th>
                <th>Status</th>
                <th>Action</th>
            </tr>
        </thead>
        <tbody>
            <?php foreach($payments as $p){ ?>

            <tr>
                <td><?php echo ($p['trx_id']); ?></td>
                <td><?php echo htmlspecialchars($p['username']); ?></td>
                <td><?php echo htmlspecialchars($p['course_code']); ?></td>
                <td><?php echo htmlspecialchars($p['approval']); ?></td>

                <td>
                    <?php if($p['approval']!='Approved'){ ?>
                    
                    <a class="btn btn-info" href="manage-enrollment.php?trx_id=<?= $p['trx_id']?>">Approve</a>
                    <?php }else { ?>
                    <button class="btn btn-secondary disables">Approved</button>

                    <?php } ?>
                    

                </td>
            </tr>

            <?php } ?>

        </tbody>
    </table>

</section>
