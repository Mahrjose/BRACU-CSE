<?php 

// Include the TCPDF library
require_once('tcpdf/tcpdf.php');

// Create new PDF object
$pdf = new TCPDF(PDF_PAGE_ORIENTATION, PDF_UNIT, PDF_PAGE_FORMAT, true, 'UTF-8', false);

// Set document information
$pdf->SetCreator(PDF_CREATOR);
$pdf->SetAuthor('Your Name');
$pdf->SetTitle('PDF Document');
$pdf->SetSubject('Example');

// Add a page
$pdf->AddPage();

// Set font
$pdf->SetFont('times', '', 12);

// Add some content
$html = '<h1>Hello, World!</h1>';
$pdf->writeHTML($html, true, false, true, false, '');

// Output the PDF as a download
$pdf->Output('example.pdf', 'D');



?>
