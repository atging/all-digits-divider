# AllDigitsDivider
# Division function that displays all of the digits
# for very large or very precise values
# (i.e., not just the first significant digits due to
# the size limits of float numbers)
# For example: 9876543211234567890/3 = 3.2921810704115226e+18,
# what is the 18th digit?
#
# Copyright 2022 Andrew Ging
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import math


def AllDigitsDivider(numerator, denominator, sigDigs=0, subsequent=False):
    # returns list of all digits of numerator divided by denominator
    # e.g., [1, 2, '.', 3, 4]
    # sigDigs is the number of digits of precision desired after the
    #   decimal point, default zero (there will be a trailing . if digits
    #   were truncated after the decimal point)

    result = []
    if subsequent is False:
        decimalAdded = False

        denomArray, decimalPosition = digitArray(denominator)
        if decimalPosition > -1:
            exponent = len(denomArray) - 1 - decimalPosition
            denominator = int(denominator * 10**exponent)
            numerator *= 10**exponent
            if int(numerator) == numerator:
                numerator = int(numerator)  # eliminate trailing '.0'
    else:
        decimalAdded = True

    numerator, trash = digitArray(numerator)

    carrier = 0

    for i, n in enumerate(numerator):

        if subsequent is True and len(result) > sigDigs:
            break

        if n != '.':  # i.e., is a 0-9 digit
            carrier = 10 * carrier + n  # appends n

            if denominator < carrier:
                quotient = math.floor(carrier / denominator)
                result.append(quotient)
                remainder = carrier - (quotient * denominator)

                carrier = remainder

            elif denominator == n:
                result.append(1)
                carrier = 0

            else:
                if (subsequent is False) and (len(result) > 0):  # don't append a leading zero
                    result.append(0)
                # elif subsequent is True:
                #     result.append(0)

            if i == len(numerator) - 1:  # if last digit
                if carrier > 0:
                    carrier *= 10
                    if decimalAdded is False:
                        result.append('.')
                        decimalAdded = True
                    if sigDigs > 0:
                        sigDigs -= 1
                        afterDecimal = AllDigitsDivider(carrier, denominator, sigDigs, True)
                        
                        for d in afterDecimal:
                            result.append(d)

                    carrier = 0
        else:
            if decimalAdded is False:
                result.append('.')
                decimalAdded = True
            else:
                print("There is more than 1 decimal point in the input")

    return result


def digitArray(number):
    # returns list of single digits from number
    # e.g., [1, 2, '.', 3, 4]
    # and index of the location of the decimal point
    # or -1 if there is no decimal point

    decimalIndex = -1

    result = []
    for i, d in enumerate(str(number)):
        if str.isdigit(d):
            result.append(int(d))
        elif d == '.':
            result.append(d)
            decimalIndex = i
        else:
            print('Number has an incorrect character:', d)

    return result, decimalIndex
