<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8" />
  <meta http-equiv="X-UA-Compatible" content="IE=edge" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
   <title>Coding Club GHRIET</title>

  <!-- bootstrap  -->
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet"
    integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous" />
  <!-- <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.10.2/dist/umd/popper.min.js" integrity="sha384-7+zCNj/IqJ95wo16oMtfsKbZ9ccEh31eOz1HGyDuCQ6wgnyJNSYdrPa03rtR1zdB" crossorigin="anonymous"></script> -->
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.min.js"
    integrity="sha384-QJHtvGhmr9XOIpI6YVutG+2QOK9T+ZnN4kzFN1RtK3zEFEIsxhlmWl5/YESvpZ13"
    crossorigin="anonymous"></script>

  <!-- bootstrap icons -->
  <link rel="stylesheet"
    href="https://cdnjs.cloudflare.com/ajax/libs/bootstrap-icons/1.8.0/font/bootstrap-icons.min.css"
    integrity="sha512-H4E1ASW8Ru1Npd1wQPB7JClskV8Nv1FG/bXK6TWMD+U9YMlR+VWUZp7SaIbBVBV/iRtefsIsv9dLSN6fdUI36w=="
    crossorigin="anonymous" referrerpolicy="no-referrer" />

  <link rel="stylesheet" href="assets/css/styles.css">

</head>

<body>
  <!-- Navbar -->
  <nav class="navbar fixed-top navbar-expand-lg navbar-dark" id="navBar"
    style="scroll-behavior: smooth; transition: 1s">
    <div class="container-fluid">
      <div style="height: 60px;">
      <a class="navbar-brand fs-3" href="#">
        <!-- coding club logo svg -->
        <img class="cc-logo" src="assets/img/cc-wot bgrmvd.png" width="55">
        <div class="cc-font">
        <div>
          < CODING
        </div>
        <div id='club-font'>
          CLUB >
        </div>
      </div>
      </a>
    </div>
      <!-- tongle btn for navbar on small viewport -->
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav"
        aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse justify-content-end" id="navbarNav">
        <ul class="navbar-nav">
          <li class="nav-item px-5">
            <!-- navbar item #1 -->
            <a class="nav-link fs-5" href="#" style="font-weight: 600">Home</a>
          </li>
          <li class="nav-item px-5">
            <!-- navbar item #2 -->
            <a class="nav-link fs-5" href="#" style="font-weight: 600">Events</a>
          </li>
          <li class="nav-item px-5">
            <!-- navbar item #3 -->
            <a class="nav-link fs-5" href="#" style="font-weight: 600">Gallery</a>
          </li>
          <li class="nav-item px-5">
            <!-- navbar item #4 -->
            <a class="nav-link fs-5" href="#" style="font-weight: 600">About Us</a>
          </li>
        </ul>
      </div>
    </div>
  </nav>

  <!-- Home section -->
  <img src="assets\img\home.png" class="img-fluid" />

  <!-- <section id="section-start" style="
    background: url('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTxm9cY7fIGnATxLao_E3Ucqmmvd6o_gwi0gw&usqp=CAU')
      0% 0% / cover no-repeat fixed;
  ">
    <div class="container" style="background-size: cover">
      <div class="row align-items-center" style="background-size: cover">
        <img src="assets\img\home.png" class="img-fluid" />
      </div>
    </div>
  </section> -->

  <!-- Welcome section -->
  <section id="section-about" class="py-5" style="
        background: url('https://media.istockphoto.com/videos/neon-abstract-background-of-blue-lines-video-id1201968269?s=640x640')
          0% 0% / cover no-repeat fixed;
      ">
    <div class="container" style="background-size: cover">
      <div class="row align-items-center" style="background-size: cover">
        <div class="col-lg-6 text-white">
          <h2>Welcome to Coding Club</h2>
          <p>
            Lorem, ipsum dolor sit amet consectetur adipisicing elit. Sed
            delectus officiis aut culpa pariatur et molestiae, minima nostrum
            debitis? dolores et quas molestias excepturi sint occaecati
            cupiditate non provident, similique sunt in culpa qui officia
            deserunt mollitia animi, id est laborum et dolorum fuga. Et harum
            quidem rerum facilis est et expedita distinctio.
          </p>

          <a href="#" class="btn btn-lg btn-danger text-white my-1">About Us</a>
        </div>

        <div class="col-lg-6 mb-sm-30">
          <div class="de-images" style="background-size: cover">
            <div id="carouselExampleControls" class="carousel slide" data-bs-ride="carousel">
              <div class="carousel-inner">
                <div class="carousel-item active">
                  <img src="assets/img/home.png" class="d-block w-100" alt="img" />
                </div>
                <div class="carousel-item">
                  <img src="assets/img/home.png" class="d-block w-100" alt="img" />
                </div>
                <div class="carousel-item">
                  <img src="assets/img/home.png" class="d-block w-100" alt="img" />
                </div>
              </div>
              <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleControls"
                data-bs-slide="prev">
                <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                <span class="visually-hidden">Previous</span>
              </button>
              <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleControls"
                data-bs-slide="next">
                <span class="carousel-control-next-icon" aria-hidden="true"></span>
                <span class="visually-hidden">Next</span>
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- features section -->
  <section id="section-features" class="py-5" style="
        background: url('https://img.rawpixel.com/s3fs-private/rawpixel_images/website_content/rm251-aum-13-g.jpg?w=1200&h=1200&dpr=1&fit=clip&crop=default&fm=jpg&q=75&vib=3&con=3&usm=15&cs=srgb&bg=F4F4F3&ixlib=js-2.2.1&s=fbcd0cdb80b3342ce32a17174f6c2024')
          0% 0% / cover no-repeat fixed;
      ">
    <!-- <div class="wm wm-border dark wow fadeInDown  animated" style="visibility: visible; animation-name: fadeInDown; background-size: cover;">features</div> -->
    <div class="container text-white" style="background-size: cover">
      <div class="row" style="background-size: cover;">
        <div class="col-md-6 offset-md-3 pb-3">
          <h1>Why you should Join Event</h1>
        </div>

        <div class="col-lg-4">
          <div class="text" style="background-size: cover">
            <h3><span>Reason 1</span></h3>
            <p>
              Lorem, ipsum dolor sit amet consectetur adipisicing elit. Sed
              delectus officiis aut culpa pariatur et molestiae, minima
              nostrum debitis?
            </p>
          </div>
        </div>

        <div class="col-lg-4">
          <div class="text" style="background-size: cover">
            <h3><span>Reason 2</span></h3>
            <p>
              Lorem, ipsum dolor sit amet consectetur adipisicing elit. Sed
              delectus officiis aut culpa pariatur et molestiae, minima
              nostrum debitis?
            </p>
          </div>
        </div>

        <div class="col-lg-4">
          <div class="text" style="background-size: cover">
            <h3><span>Reason 3</span></h3>
            <p>
              Lorem, ipsum dolor sit amet consectetur adipisicing elit. Sed
              delectus officiis aut culpa pariatur et molestiae, minima
              nostrum debitis?
            </p>
          </div>
        </div>

        <div class="col-lg-4">
          <div class="text" style="background-size: cover">
            <h3><span>Reason 4</span></h3>
            <p>
              Lorem, ipsum dolor sit amet consectetur adipisicing elit. Sed
              delectus officiis aut culpa pariatur et molestiae, minima
              nostrum debitis?
            </p>
          </div>
        </div>

        <div class="col-lg-4">
          <div class="text" style="background-size: cover">
            <h3><span>Reason 5</span></h3>
            <p>
              Lorem, ipsum dolor sit amet consectetur adipisicing elit. Sed
              delectus officiis aut culpa pariatur et molestiae, minima
              nostrum debitis?
            </p>
          </div>
        </div>

        <div class="col-lg-4">
          <div class="text" style="background-size: cover">
            <h3><span>Reason 6</span></h3>
            <p>
              Lorem, ipsum dolor sit amet consectetur adipisicing elit. Sed
              delectus officiis aut culpa pariatur et molestiae, minima
              nostrum debitis?
            </p>
          </div>
        </div>
      </div>
    </div>
  </section>


  <!-- Registration Section -->
  <section id="section-registration" class="py-5" style="
        background: url('https://as1.ftcdn.net/v2/jpg/02/29/54/36/1000_F_229543694_HMybtq6QIco9J6X2puiu8FuvKYXn5JOC.jpg')
          0% 50% / cover no-repeat fixed;
      ">
    <div class="container" style="background-size: cover">
      <div class="row align-items-center" style="background-size: cover">
        <div class="text-center text-white">
          <h1>Registration Form</h1>
        </div>
        <div class="text-white">
          <p>Lorem, ipsum dolor sit amet consectetur adipisicing elit. Perspiciatis tempora laboriosam dolore, explicabo
            velit eveniet saepe, perferendis praesentium iure repellat a, nemo asperiores nihil optio. Eum atque ratione
            quas suscipit?
            Laborum eos totam odit sapiente, beatae magnam provident ratione harum sit? Sequi quisquam, aliquam quo
            cumque reprehenderit quas nulla! Laboriosam, vero? Ipsa accusamus voluptates culpa ab exercitationem nam
            aliquam dolorum.
            Cupiditate eum ea minus explicabo, nisi quis perferendis deserunt harum quasi voluptatem? Atque odit autem
            architecto sequi blanditiis, dolorem voluptatem quis laudantium vitae libero aliquam quae officia, culpa,
            nulla distinctio.
            Dignissimos, quam cum. Porro earum adipisci iusto iure. Laborum voluptates veniam ab sed! Dolore illum
            dolores officia laborum voluptatum quisquam, error distinctio nemo blanditiis voluptatem quis eveniet
            ratione? Blanditiis, perspiciatis.
            Velit fugiat magnam officiis corrupti quos veritatis ratione explicabo dicta accusantium, fugit incidunt
            nihil laudantium voluptate ipsa doloribus earum praesentium ipsam? Error earum consectetur quibusdam laborum
            quasi quisquam dicta vitae!
            Non, neque excepturi perferendis explicabo, optio doloremque consectetur modi sit corporis dolorem delectus
            ducimus pariatur natus minima ipsum eum, deserunt fugit blanditiis magni voluptas reiciendis! Dolore libero
            iste ducimus error.
            Fugit accusamus voluptates sint ipsam blanditiis? Asperiores eligendi debitis aut, totam dolorum, illo
            repellat nam voluptatibus nobis veritatis facere enim harum labore! Quia tempora, sed voluptate unde
            molestias eveniet! Quia?
            Molestias, sapiente. Unde, obcaecati, porro minima veritatis impedit deserunt doloremque adipisci aliquam
            eos saepe quisquam optio reprehenderit, dolores dicta expedita numquam atque hic tenetur sint corrupti
            eveniet ratione. Asperiores, quia.
            Delectus autem laboriosam doloribus consectetur similique voluptates vitae facilis velit! Officiis
            accusamus, explicabo odit minus consectetur numquam tenetur, earum nemo quam nulla vero obcaecati facere
            enim! Deserunt ad illum deleniti!
            Asperiores rerum soluta earum, nesciunt eligendi, et quia quidem accusamus tempore doloribus vel aspernatur.
            Tempore et nihil reiciendis error. Saepe sed repellat totam quis vero commodi asperiores quas mollitia
            architecto.
            Amet consequatur quas possimus! Ullam rerum nemo adipisci et recusandae voluptas amet similique autem animi
            quis rem veritatis dignissimos, porro doloremque deserunt quod aspernatur reprehenderit eius quas optio
            perferendis eum.
            Quibusdam doloribus veritatis nostrum amet odio dicta perferendis sequi error quos quaerat iste ipsam in
            libero aut quod, numquam doloremque nisi maxime nesciunt laboriosam et molestiae expedita non soluta.
            Cumque.
            Voluptate modi consequuntur sapiente dolorum maxime alias ab molestiae cupiditate, pariatur excepturi. Quam
            recusandae quos voluptas amet necessitatibus voluptate aperiam nulla nesciunt dolores tempora. Consectetur
            magnam quo dolore rerum cupiditate!
            Minus provident eveniet dignissimos minima nesciunt. Sunt, magnam minima enim nihil libero repudiandae et
            harum dicta atque, facere molestias vitae eum! Ipsa expedita commodi quaerat aut, facilis sequi blanditiis
            sit!
            Sequi ad laudantium necessitatibus nisi maiores assumenda quo architecto illum non unde tempora eum
            cupiditate, aliquam numquam vitae repellendus omnis accusamus. Qui vero omnis, explicabo non hic quia
            dolorem porro?
            Repudiandae distinctio sint unde modi velit vel exercitationem totam quaerat. Architecto aliquam explicabo,
            voluptatibus a voluptatum tempora sit in provident accusantium aperiam qui facilis placeat cum dolorum
            eaque, recusandae eum!
            Necessitatibus ea perferendis expedita. Excepturi ad illum quos ex! Explicabo, ex tenetur obcaecati repellat
            natus ut eligendi magnam distinctio, id libero ullam hic mollitia. Excepturi totam odio dolorum recusandae
            illum!
            Recusandae inventore nemo esse facere aliquam. Voluptatum voluptate beatae praesentium, placeat labore quis
            exercitationem accusantium dicta a voluptatibus quo, magni explicabo recusandae iste suscipit ut quibusdam
            nobis quae nostrum natus?
            Excepturi quod voluptatum dolorem nesciunt voluptates accusamus alias, veniam pariatur iste molestias, vero
            aspernatur. Dolorem nostrum repudiandae voluptates ratione, nemo sit cumque. Cupiditate totam incidunt,
            facere unde quidem sunt repellendus!
            Consectetur rem explicabo officia ex ratione nesciunt asperiores cupiditate maiores hic excepturi dicta
            reiciendis earum consequatur doloribus quidem tempore, quod labore obcaecati corporis nemo ipsam
            necessitatibus. Tempora quidem eligendi corporis.</p>
        </div>
      </div>
  </section>


  <!-- Footer Section -->

  <section id="section-registration" class="py-5" style="
        background-color: black;
      ">
    <div class="container" style="background-size: cover">
      <div class="row align-items-center" style="background-size: cover">
        <div class="col-md-3" style="background-size: cover;">
          <img src="assets/img/CC-logo.png" class="logo-small" alt="" width="50"><br>
        </div>

        <div class="col-md-6 text-white" style="background-size: cover;">
          <div class="fs-3"> Coding Club </div><span class="id-color"> GH Raisoni Institute Of Engineering and Technology,
            Nagpur</span>
        </div>

        <div class="col-md-3 text-white " style="background-size: cover;">
          <div class="social-icons" style="background-size: cover;">
            <a href="#"><i class="bi-facebook " style="font-size: xx-large;"></i></a>
            <a href="#"><i class="bi-instagram " style="font-size: xx-large; color:  #E1306C;"></i></a>
            <a href="#"><i class="bi-linkedin " style="font-size: xx-large; color: #0e76a8;"></i></a>
          </div>
        </div>
      </div>
    </div>
  </section>

<script type="text/javascript" src="assets/js/main.js"></script>
</body>
</html>