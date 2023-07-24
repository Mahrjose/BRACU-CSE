<?php 
session_start();

require_once 'config/dbconnect.php';
require_once 'config/classes/Users.php';
require_once 'config/classes/Courses.php';

$c = new Courses();
$u = new User();
// $b = new Blogs();

?>


<!DOCTYPE html>
<html lang="en">

  <head>

    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta name="description" content="">
    <meta name="author" content="">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@100;200;300;400;500;600;700;800;900&display=swap" rel="stylesheet">

    <title>OCW - Course Hibe</title>

    <!-- Bootstrap core CSS -->
    <link href="assets/homepage/vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet">


    <!-- Additional CSS Files -->
    <link rel="stylesheet" href="assets/homepage/assets/css/fontawesome.css">
    <link rel="stylesheet" href="assets/homepage/assets/css/all.css">
    <link rel="stylesheet" href="assets/homepage/assets/css/animated.css">
    <link rel="stylesheet" href="assets/homepage/assets/css/owl.css">

  </head>

<body>

  <!-- ***** Preloader Start ***** -->
  <div id="js-preloader" class="js-preloader">
    <div class="preloader-inner">
      <span class="dot"></span>
      <div class="dots">
        <span></span>
        <span></span>
        <span></span>
      </div>
    </div>
  </div>
  <!-- ***** Preloader End ***** -->

  <!-- Pre-header Starts -->
  <!-- <div class="pre-header">
    <div class="container">
      <div class="row">
        <div class="col-lg-8 col-sm-8 col-7">
          <ul class="info">
            <li><a href="#"><i class="fa fa-envelope"></i>digimedia@company.com</a></li>
            <li><a href="#"><i class="fa fa-phone"></i>010-020-0340</a></li>
          </ul>
        </div>
        <div class="col-lg-4 col-sm-4 col-5">
          <ul class="social-media">
            <li><a href="#"><i class="fa fa-facebook"></i></a></li>
            <li><a href="#"><i class="fa fa-behance"></i></a></li>
            <li><a href="#"><i class="fa fa-twitter"></i></a></li>
            <li><a href="#"><i class="fa fa-dribbble"></i></a></li>
          </ul>
        </div>
      </div>
    </div>
  </div> -->
  <!-- Pre-header End

  <!-- ***** Header Area Start ***** -->
  <header class="header-area header-sticky wow slideInDown" data-wow-duration="0.75s" data-wow-delay="0s" style="z-index:10">
    <div class="container">
      <div class="row">
        <div class="col-12">
          <nav class="main-nav">
            <!-- ***** Logo Start ***** -->
            <a href="/OCW" class="logo">
              <!-- <img src="assets/images/logo-v3.png" alt=""> -->
              <span style="font-size:32px; font-weight:700">OCW.</span>
            </a>
            <!-- ***** Logo End ***** -->
            <!-- ***** Menu Start ***** -->
            <ul class="nav">
              <li class="scroll-to-section"><a href="/OCW" class="active">Home</a></li>
              <li class="scroll-to-section"><a href="">About</a></li>
              <li class="scroll-to-section"><a href="#services">OCW Special</a></li>
              <li class="scroll-to-section"><a href="all-courses.php">Courses</a></li>
              <li class="scroll-to-section"><a href="blogs">Blog</a></li>
              <li class="scroll-to-section"><a href="#contact">Contact</a></li>
              
              <?php if(!isset($_SESSION['username'])){ ?>
              
                <li class="scroll-to-section"><a href="login.php">Login</a></li>
                <li class="">
                    <div class="border-first-button"><a href="sign-up.php">Signup</a></div>
                </li> 

              <?php }else { ?>
              <li class="scroll-to-section"><a href="user.php"><i class="fa fa-user"></i> Profile</a></li>
              <?php } ?>
              

              
            </ul>        
            <a class='menu-trigger'>
                <span>Menu</span>
            </a>
            <!-- ***** Menu End ***** -->
          </nav>
        </div>
      </div>
    </div>
  </header>
  <!-- ***** Header Area End ***** -->

  <!-- Hero Section Banner Start -->

  <div class="main-banner wow fadeIn" id="top" data-wow-duration="1s" data-wow-delay="0.5s">
    <div class="container">
      <div class="row">
        <div class="col-lg-12">
          <div class="row">
            <div class="col-lg-6 align-self-center">
              <div class="left-content show-up header-text wow fadeInLeft" data-wow-duration="1s" data-wow-delay="1s">
                <div class="row">
                  <div class="col-lg-12">
                    <h6>Infinity Courseware</h6>
                    <h2>All your academic and Skill courses</h2>
                    <p>This opencourseware platform will boost your learning in next level. No more excuses for not having enough resources. You are just one click away from your dream. Start Learning!</p>
                  </div>
                  <div class="col-lg-12">
                    <div class="border-first-button scroll-to-section">
                      <a href="#contact">Explore Courses</a>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <div class="col-lg-6">
              <div class="right-image wow fadeInRight" data-wow-duration="1s" data-wow-delay="0.5s">
                <img src="assets/homepage/assets/images/Online learning-bro.png" alt="">
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>

  <div id="about" class="about section">
    <div class="container">
      <div class="row">
        <div class="col-lg-12">
          <div class="row">
            <div class="col-lg-6">
              <div class="about-left-image  wow fadeInLeft" data-wow-duration="1s" data-wow-delay="0.5s">
                <img src="assets/homepage/assets/images/Course app-pana.png" alt="">
              </div>
            </div>
            <div class="col-lg-6 align-self-center  wow fadeInRight" data-wow-duration="1s" data-wow-delay="0.5s">
              <div class="about-right-content">
                <div class="section-heading">
                  <h6>About OCW</h6>
                  <h4>About <em>OCW</em></h4>
                  <div class="line-dec"></div>
                </div>
                <p>We hope this OCW platform is useful for your learning. You can enroll free and premium courses. You can <a rel="nofollow" href="http://paypal.me/templatemo" target="_blank">Explore</a> courses or <a href="https://templatemo.com/contact" target="_blank">Join</a> Discussion forum</p>
                <div class="row">
                  <div class="col-lg-4 col-sm-4">
                    <div class="skill-item first-skill-item wow fadeIn" data-wow-duration="1s" data-wow-delay="0s">
                      <div class="progress" data-percentage="90">
                        <span class="progress-left">
                          <span class="progress-bar"></span>
                        </span>
                        <span class="progress-right">
                          <span class="progress-bar"></span>
                        </span>
                        <div class="progress-value">
                          <div>
                            90%<br>
                            <span>Coding</span>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                  <div class="col-lg-4 col-sm-4">
                    <div class="skill-item second-skill-item wow fadeIn" data-wow-duration="1s" data-wow-delay="0s">
                      <div class="progress" data-percentage="80">
                        <span class="progress-left">
                          <span class="progress-bar"></span>
                        </span>
                        <span class="progress-right">
                          <span class="progress-bar"></span>
                        </span>
                        <div class="progress-value">
                          <div>
                            80%<br>
                            <span>Photoshop</span>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                  <div class="col-lg-4 col-sm-4">
                    <div class="skill-item third-skill-item wow fadeIn" data-wow-duration="1s" data-wow-delay="0s">
                      <div class="progress" data-percentage="80">
                        <span class="progress-left">
                          <span class="progress-bar"></span>
                        </span>
                        <span class="progress-right">
                          <span class="progress-bar"></span>
                        </span>
                        <div class="progress-value">
                          <div>
                            80%<br>
                            <span>Animation</span>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div> 
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>

  <div id="services" class="services section">
    <div class="container">
      <div class="row">
        <div class="col-lg-12">
          <div class="section-heading  wow fadeInDown" data-wow-duration="1s" data-wow-delay="0.5s">
            <h6></h6>
            <h4>What Opencourseware <em>Provides</em></h4>
            <div class="line-dec"></div>
          </div>
        </div>
        <div class="col-lg-12">
          <div class="naccs">
            <div class="grid">
              <div class="row">
                <div class="col-lg-12">
                  <div class="menu">
                    <div class="first-thumb active">
                      <div class="thumb">
                        <span class="icon"><img src="assets/images/service-icon-01.png" alt=""></span>
                        Courses
                      </div>
                    </div>
                    <div>
                      <div class="thumb">                 
                        <span class="icon"><img src="assets/images/service-icon-02.png" alt=""></span>
                        Resources
                      </div>
                    </div>
                    <div>
                      <div class="thumb">                 
                        <span class="icon"><img src="assets/images/service-icon-03.png" alt=""></span>
                        Discussion Forum
                      </div>
                    </div>
                    <div class="last-thumb">
                      <div class="thumb">                 
                        <span class="icon"><img src="assets/images/service-icon-01.png" alt=""></span>
                        Articles
                      </div>
                    </div>
                  </div>
                </div> 

                <div class="col-lg-12">
                  <ul class="nacc">
                    <li class="active">
                      <div>
                        <div class="thumb">
                          <div class="row">
                            <div class="col-lg-6 align-self-center">
                              <div class="left-text">
                                <h4>Courses &amp; </h4>
                                <p>Enroll the best picked courses. Instructed by the world class mentor.</p>
                                <div class="ticks-list"><span><i class="fa fa-check"></i> Self paced</span> <span><i class="fa fa-check"></i> Data Info</span> <span><i class="fa fa-check"></i>Easily explained</span>
                                  <span><i class="fa fa-check"></i>Access from anywhere</span> <span><i class="fa fa-check"></i>Free & paid courses</span> <span><i class="fa fa-check"></i> Optimized Template</span></div>
                                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sedr do eiusmod deis tempor incididunt.</p>
                              </div>
                            </div>
                            <div class="col-lg-6 align-self-center">
                              <div class="right-image">
                                <img src="assets/images/services-image.jpg" alt="">
                              </div>
                            </div>
                          </div>
                        </div>
                      </div>
                    </li>
                    <li>
                      <div>
                        <div class="thumb">
                          <div class="row">
                            <div class="col-lg-6 align-self-center">
                              <div class="left-text">
                                <h4>Healthy Food &amp; Life</h4>
                                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sedr do eiusmod deis tempor incididunt ut labore et dolore kengan darwin doerski token.
                                  dover lipsum lorem and the others.</p>
                                <div class="ticks-list"><span><i class="fa fa-check"></i> Optimized Template</span> <span><i class="fa fa-check"></i> Data Info</span> <span><i class="fa fa-check"></i> SEO Analysis</span>
                                  <span><i class="fa fa-check"></i> Data Info</span> <span><i class="fa fa-check"></i> SEO Analysis</span> <span><i class="fa fa-check"></i> Optimized Template</span></div>
                                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sedr do eiusmod deis tempor incididunt.</p>
                              </div>
                            </div>
                            <div class="col-lg-6 align-self-center">
                              <div class="right-image">
                                <img src="assets/images/services-image-02.jpg" alt="">
                              </div>
                            </div>
                          </div>
                        </div>
                      </div>
                    </li>
                    <li>
                      <div>
                        <div class="thumb">
                          <div class="row">
                            <div class="col-lg-6 align-self-center">
                              <div class="left-text">
                                <h4>Car Re-search &amp; Transport</h4>
                                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sedr do eiusmod deis tempor incididunt ut labore et dolore kengan darwin doerski token.
                                  dover lipsum lorem and the others.</p>
                                <div class="ticks-list"><span><i class="fa fa-check"></i> Optimized Template</span> <span><i class="fa fa-check"></i> Data Info</span> <span><i class="fa fa-check"></i> SEO Analysis</span>
                                  <span><i class="fa fa-check"></i> Data Info</span> <span><i class="fa fa-check"></i> SEO Analysis</span> <span><i class="fa fa-check"></i> Optimized Template</span></div>
                                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sedr do eiusmod deis tempor incididunt.</p>
                              </div>
                            </div>
                            <div class="col-lg-6 align-self-center">
                              <div class="right-image">
                                <img src="assets/images/services-image-03.jpg" alt="">
                              </div>
                            </div>
                          </div>
                        </div>
                      </div>
                    </li>
                    <li>
                      <div>
                        <div class="thumb">
                          <div class="row">
                            <div class="col-lg-6 align-self-center">
                              <div class="left-text">
                                <h4>Online Shopping &amp; Tracking ID</h4>
                                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sedr do eiusmod deis tempor incididunt ut labore et dolore kengan darwin doerski token.
                                  dover lipsum lorem and the others.</p>
                                <div class="ticks-list"><span><i class="fa fa-check"></i> Optimized Template</span> <span><i class="fa fa-check"></i> Data Info</span> <span><i class="fa fa-check"></i> SEO Analysis</span>
                                  <span><i class="fa fa-check"></i> Data Info</span> <span><i class="fa fa-check"></i> SEO Analysis</span> <span><i class="fa fa-check"></i> Optimized Template</span></div>
                                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sedr do eiusmod deis tempor incididunt.</p>
                              </div>
                            </div>
                            <div class="col-lg-6 align-self-center">
                              <div class="right-image">
                                <img src="assets/images/services-image-04.jpg" alt="">
                              </div>
                            </div>
                          </div>
                        </div>
                      </div>
                    </li>
                  </ul>
                </div>          
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>

  
  <div id="free-quote" class="free-quote">
    <div class="container">
      <div class="row">
        <div class="col-lg-4 offset-lg-4">
          <div class="section-heading  wow fadeIn" data-wow-duration="1s" data-wow-delay="0.3s">
            <h6>Get Your Free Quote</h6>
            <h4>Grow With Us Now</h4>
            <div class="line-dec"></div>
          </div>
        </div>
        <div class="col-lg-8 offset-lg-2  wow fadeIn" data-wow-duration="1s" data-wow-delay="0.8s">
          <form id="search" action="#" method="GET">
            <div class="row">
              <div class="col-lg-4 col-sm-4">
                <fieldset>
                  <input type="web" name="web" class="website" placeholder="Your website URL..." autocomplete="on" required>
                </fieldset>
              </div>
              <div class="col-lg-4 col-sm-4">
                <fieldset>
                  <input type="address" name="address" class="email" placeholder="Email Address..." autocomplete="on" required>
                </fieldset>
              </div>
              <div class="col-lg-4 col-sm-4">
                <fieldset>
                  <button type="submit" class="main-button">Get Quote Now</button>
                </fieldset>
              </div>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>


  <div id="portfolio" class="top-courses section">
    <div class="container">
      <div class="row">
        <div class="col-lg-5">
          <div class="section-heading wow fadeInLeft" data-wow-duration="1s" data-wow-delay="0.3s">
            <h6>Top Picks</h6>
            <h4>Explore popular <em>Courses</em></h4>
            <div class="line-dec"></div>
          </div>
        </div>
      </div>
    </div>


    <!-- Fetch dynamic courses from backend -->
    <?php 

        $courses = $c->getLatestCourses();
    ?>
    

    <div class="container-fluid wow fadeIn" data-wow-duration="1s" data-wow-delay="0.7s">
      <div class="row">
        <div class="col-lg-12">
          <div class="loop owl-carousel">

          <?php foreach($courses as $course){ ?>
                <div class="item">
                    <a href="all-courses.php?course_code=<?= $course['course_code']?>">
                        <div class="portfolio-item">
                            <div class="thumb">
                            <img src="./blogs/upload/<?=$course['thumbnail']?>" alt="">
                            </div>
                            <div class="down-content">
                                <h4><?=$course['course_code'] ?></h4>
                                <span><?=$course['course_title']?></span>
                            </div>
                        </div>
                    </a>  
                </div>

           <?php } ?>

           <!-- Courses ends -->
          </div>
        </div>
      </div>
    </div>
  </div>
  



<!-- Fetch recent blog from database -->

    <?php $blogs = $u->getRecentBlogs();?>

  <div id="blog" class="blog">
    <div class="container">
      <div class="row">
        <div class="col-lg-4 offset-lg-4  wow fadeInDown" data-wow-duration="1s" data-wow-delay="0.3s">
          <div class="section-heading">
            <h6>Recent Articles</h6>
            <h4>Check Our Blog <em>Posts</em></h4>
            <div class="line-dec"></div>
          </div>
        </div>

        <div class="col-lg-6 show-up wow fadeInUp" data-wow-duration="1s" data-wow-delay="0.3s">
        
          <div class="blog-post">
            <div class="thumb">
              <a href="#"><img src="assets/images/blog-post-01.jpg" alt=""></a>
            </div>
            <div class="down-content">
              <span class="category"><?= $blogs[0]['category']?></span>
              <span class="date"><?= $blogs[0]['publish']?></span>
              <a href="#"><h4><?= $blogs[0]['post_title']?></h4></a>
              <p><?php if(strlen($blogs[0]['post_content'])>15){
                    $msg = "";
                    for($i = 0; $i<15; $i++){
                        $msg += $blogs[0]['post_content'][$i];
                    }
                    echo $msg;
                    }else echo $blogs[0]['post_content'];?>
              </p>
              <span class="author"><img src="assets/images/author-post.jpg" alt="">By: Andrea Mentuzi</span>
              <div class="border-first-button"><a href="blogs/">Discover More</a></div>
            </div>
          </div>
        </div>

        <div class="col-lg-6 wow fadeInUp" data-wow-duration="1s" data-wow-delay="0.3s">
          <div class="blog-posts">
            <div class="row">
            <?php for($x = 1; $x<count($blogs); $x++){ ?>
                <div class="col-lg-12">
                
                    <div class="post-item my-2">
                    <div class="thumb">
                        <a href="#"><img src="assets/images/blog-post-03.jpg" alt=""></a>
                    </div>
                    <div class="right-content">
                        <span class="category"><?= $blogs[$x]['category']?></span>
                        <span class="date"><?=$blogs[$x]['publish']?></span>
                        <a href="#"><h4><?= $blogs[$x]['post_title']?></h4></a>
                        <p>
                        </p>
                    </div>
                    </div>
                </div>
            <?php }?>
            
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>  



  <div id="contact" class="contact-us section">
    <div class="container">
      <div class="row">
        <div class="col-lg-6 offset-lg-3">
          <div class="section-heading wow fadeIn" data-wow-duration="1s" data-wow-delay="0.5s">
            <h6>Contact Us</h6>
            <h4>Get In Touch With Us <em>Now</em></h4>
            <div class="line-dec"></div>
          </div>
        </div>
        <div class="col-lg-12 wow fadeInUp" data-wow-duration="0.5s" data-wow-delay="0.25s">
          <form id="contact" action="" method="post">
            <div class="row">
              <div class="col-lg-12">
                <div class="contact-dec">
                  <img src="assets/images/contact-dec-v3.png" alt="">
                </div>
              </div>
              <div class="col-lg-5">
                <div id="map">
                  <iframe src="https://maps.google.com/maps?q=Av.+L%C3%BAcio+Costa,+Rio+de+Janeiro+-+RJ,+Brazil&t=&z=13&ie=UTF8&iwloc=&output=embed" width="100%" height="636px" frameborder="0" style="border:0" allowfullscreen></iframe>
                </div>
              </div>
              <div class="col-lg-7">
                <div class="fill-form">
                  <div class="row">
                    <div class="col-lg-4">
                      <div class="info-post">
                        <div class="icon">
                          <img src="assets/images/phone-icon.png" alt="">
                          <a href="#">010-020-0340</a>
                        </div>
                      </div>
                    </div>
                    <div class="col-lg-4">
                      <div class="info-post">
                        <div class="icon">
                          <img src="assets/images/email-icon.png" alt="">
                          <a href="#">our@email.com</a>
                        </div>
                      </div>
                    </div>
                    <div class="col-lg-4">
                      <div class="info-post">
                        <div class="icon">
                          <img src="assets/images/location-icon.png" alt="">
                          <a href="#">123 Rio de Janeiro</a>
                        </div>
                      </div>
                    </div>
                    <div class="col-lg-6">
                      <fieldset>
                        <input type="name" name="name" id="name" placeholder="Name" autocomplete="on" required>
                      </fieldset>
                      <fieldset>
                        <input type="text" name="email" id="email" pattern="[^ @]*@[^ @]*" placeholder="Your Email" required="">
                      </fieldset>
                      <fieldset>
                        <input type="subject" name="subject" id="subject" placeholder="Subject" autocomplete="on">
                      </fieldset>
                    </div>
                    <div class="col-lg-6">
                      <fieldset>
                        <textarea name="message" type="text" class="form-control" id="message" placeholder="Message" required=""></textarea>  
                      </fieldset>
                    </div>
                    <div class="col-lg-12">
                      <fieldset>
                        <button type="submit" id="form-submit" class="main-button ">Send Message Now</button>
                      </fieldset>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>

  <footer>
    <div class="container py-2">
      <div class="row">
        <div class="col-lg-12">
            <p style="font-size:32px">Useful Links</p>

            <div class="row footer-menu">
              <div class="col-lg-4 ">
                <ul class="footer-link">
                  <li><a href="https://www.cse.buet.ac.bd/" target="_blank">CSE Department</a></li>
                  <li><a href="https://www.buet.ac.bd/" target="_blank">BUET</a></li>
                  <li><a href="https://www.buet.ac.bd/academics/undergraduate" target="_blank">Undergraduate</a></li>
                  <li><a href="https://www.buet.ac.bd/academics/postgraduate" target="_blank">Postgraduate</a></li>
                  <li><a href="https://www.buet.ac.bd/academics/phd" target="_blank">PhD</a></li>
                </ul>
              </div>
            </div>

        </div>
        <div class="col-lg-12">
          <p>Copyright © 2023 Courseware. All Rights Reserved. 
          <br>Developed by <a href="https://syedfaysel.githu.io" target="_parent" title="free css templates">CSE370 Group Project</a></p>
        </div>

      </div>
    </div>
  </footer>





<!-- Scripts -->
<script src="assets/homepage/vendor/jquery/jquery.min.js"></script>
<script src="assets/homepagevendor/bootstrap/js/bootstrap.bundle.min.js"></script>
<script src="assets/homepage/assets/js/owl-carousel.js"></script>
<script src="assets/homepage/assets/js/animation.js"></script>
<script src="assets/homepage/assets/js/imagesloaded.js"></script>
<script src="assets/homepage/assets/js/custom.js"></script>

</body>
</html>