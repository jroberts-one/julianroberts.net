function calcuateWeeklyDistance() {
  console.log('calcuateWeeklyDistance called');
  $("#trainingTable tr:has(span.distance)").each(function() {
    let weeklySum = 0;

    $(this).find("span.distance").each(function() {
      weeklySum += parseFloat($(this).text());
    });

    $('td.total', this).html(weeklySum);
  });
}

calcuateWeeklyDistance();


$("#unitSelect").change(function() {
  console.log('change event called');

  let opt = this.value;

  $("td span.distance").each(function() {

    const factor = 0.621371; // conversion factor
    let result;
    if (opt == 'imperial') {
      // km to mi
      let kilometers = parseInt($(this).html());
      result = Math.round(kilometers * factor);

    } else if (opt == 'metric') {
      // mi to km
      let miles = parseInt($(this).html());
      result = Math.round(miles / factor);
    }
    $(this).html(result);
    calcuateWeeklyDistance();
  });
});
