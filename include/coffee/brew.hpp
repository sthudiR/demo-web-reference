#pragma once

/// @file brew.hpp
/// @brief Tiny helpers for brewing ratios.

namespace coffee {

/// @brief Supported brewing methods.
enum class Method {
  Espresso,  ///< Pressurised, short and concentrated.
  Pourover,  ///< Gravity-fed through a paper filter.
  French,    ///< Full-immersion with a metal mesh.
  ColdBrew   ///< Long, cold immersion.
};

/// @brief A recipe expressed as a ratio of water to coffee.
struct Recipe {
  Method method;      ///< How the coffee is brewed.
  double coffee_g;    ///< Dose of ground coffee in grams.
  double ratio;       ///< Grams of water per gram of coffee.
};

/// @brief Compute the water needed for a dose of coffee.
/// @param coffee_g Dose of coffee in grams.
/// @param ratio Water-to-coffee ratio (for example 16 for 1:16).
/// @return Water in grams (about the same in millilitres).
inline double water_for(double coffee_g, double ratio) { return coffee_g * ratio; }

/// @brief Estimate brew strength as total dissolved solids.
/// @param dissolved_g Grams of coffee solids in the cup.
/// @param beverage_g Grams of finished beverage.
/// @return TDS as a percentage.
inline double strength_tds(double dissolved_g, double beverage_g) {
  return 100.0 * dissolved_g / beverage_g;
}

}  // namespace coffee
