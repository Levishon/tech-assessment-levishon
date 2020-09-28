using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Mvc;
using Weather.Models;

namespace Weather.Controllers
{
    public class WeatherController : Controller
    {
        // GET: Weather
        public ActionResult GetWeather()
        {
            WeatherDBEntities1 db = new WeatherDBEntities1();
            List<Temp> temps = db.Temps.ToList<Temp>();
            return View(temps);
        }
    }
}