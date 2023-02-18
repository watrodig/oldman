<?php

// Example JSON list of popular culture events
$json = '[
    {
        "title": "Perfect Day",
        "artist": "Lou Reed",
        "releaseYear": 1972
    },
    {
        "title": "Perfect Day",
        "artist": "Lou Reed",
        "releaseYear": 1997
    },
    {
        "title": "Thriller",
        "artist": "Michael Jackson",
        "releaseYear": 1982
    },
    {
        "title": "Let It Be",
        "artist": "The Beatles",
        "releaseYear": 1970
    }
]';

// Convert the JSON string to a PHP array
$events = json_decode($json, true);

// Define the target year (e.g. 2022)
$targetYear = 2023;


// Loop through the events and compare each pair for equal year differences
for ($i = 0; $i < count($events); $i++) {
  for ($j = $i + 1; $j < count($events); $j++) {
    $event1 = $events[$i];
    $event2 = $events[$j];
    $yearDiff = abs($event2["releaseYear"] - $event1["releaseYear"]);
    if ($yearDiff > 0 && $yearDiff == $targetYear - $event2["releaseYear"]) {
      echo "The events '{$event1["title"]}' by {$event1["artist"]} ({$event1["releaseYear"]}) and '{$event2["title"]}' by {$event2["artist"]} ({$event2["releaseYear"]}) were released {$yearDiff} years apart and are equally distant from {$targetYear}.<br>";
    }
  }
}

?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Popular Culture Tool</title>
    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css"
          integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u"
          crossorigin="anonymous">
</head>
<body>
<div class="container">
    <div class="row">
        <div class="col-md-6 col-md-offset-3">
            <h1 class="text-center">You Are An Old Bastard.com</h1>
            <form method="post" action="submit.php">

                <p>Take a trip back in time</p>
                <p>We find events that are equally away in time from each other just to make you feel old as fuck!</p>
                
                <p><img src="cobain.jpeg" /></p>

                <div class="form-group">
                    <label for="year">Starting Year:</label>
                    <input type="number" class="form-control" id="year" name="year" placeholder="2023">
                </div>

                <div class="form-group">
                    <label for="from_year">From Year:</label>
                    <input type="number" class="form-control" id="from_year" name="from_year" placeholder="Enter year">
                </div>
                <div class="form-group">
                    <label for="to_year">To Year:</label>
                    <input type="number" class="form-control" id="to_year" name="to_year" placeholder="Enter year">
                </div>

                <div class="form-group">
                    <label for="name">Your Name:</label>
                    <input type="text" class="form-control" id="name" name="name" placeholder="Enter name">
                </div>

                <div class="form-group">
                    <label for="category">Category of event to time-compare</label>
                    <select class="form-control" id="category" name="category">
                        <option value="film_releases">Film Releases</option>
                        <option value="music_releases">Music Releases</option>
                        <option value="celebrity_births">Celebrity Births</option>
                        <option value="general_pop_culture">General Pop Culture</option>
                    </select>
                </div>

                <button type="submit" class="btn btn-primary">Time to appall yourself</button>
            </form>
        </div>
    </div>
</div>

<!-- jQuery -->
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
<!-- Bootstrap JS -->
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"
        integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfQgxH8J9H8hBnRHPUfvL+28dJPw7EkaGge5iJ0Wp"
        crossorigin="anonymous"></script>
</body>
</html>


