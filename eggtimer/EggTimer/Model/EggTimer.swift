//
//  EggTimer.swift
//  EggTimer
//
//  Created by clockard on 5/30/18.
//  Copyright © 2018 clockard. All rights reserved.
//

import Foundation

protocol EggTimerProtocol {
    func timeRemainingOnTimer(_ timer: EggTimer, timeRemaining: TimeInterval)
    func timerHasFinished(_ timer: EggTimer)
}

class EggTimer {
    
    var delegate: EggTimerProtocol?
    
    var timer: Timer? = nil
    var startTime: Date?
    var duration: TimeInterval = 360        // default 6 minutes
    var elapsedTime: TimeInterval = 0
    
    var isStopped: Bool {
        return timer == nil && elapsedTime == 0
    }
    var isPaused: Bool {
        return timer == nil && elapsedTime > 0
    }
    
    @objc dynamic func timerAction() {
        // startTime is an optional date - if it is nil, the timer cannot be running so nothing happens
        guard let startTime = startTime else {
            return
        }
        
        // Re-calculate the elapsedTime property. startTime is earlier than now, so timeIntervalSinceNow
        // produces a negative value. The minus sign inverts this to a positive value
        elapsedTime = -startTime.timeIntervalSinceNow
        
        // Calculate the number of seconds remaining in the timer, rounded to the nearest second
        let secondsRemaining = (duration - elapsedTime).rounded()
        
        // If the timer has finished, notify the delegate. Otherwise, tell the delegate the number of
        // seconds remaining.
        if secondsRemaining <= 0 {
            resetTimer()
            delegate?.timerHasFinished(self)
        } else {
            delegate?.timeRemainingOnTimer(self, timeRemaining: secondsRemaining)
        }
    }
    
    func startTimer() {
        startTime = Date()
        elapsedTime = 0
        
        timer = Timer.scheduledTimer(timeInterval: 1,
                                     target: self,
                                     selector: #selector(timerAction),
                                     userInfo: nil,
                                     repeats: true)
        timerAction()
    }

    func resumeTimer() {
        startTime = Date(timeIntervalSinceNow: -elapsedTime)
        
        timer = Timer.scheduledTimer(timeInterval: 1,
                                     target: self,
                                     selector: #selector(timerAction),
                                     userInfo: nil,
                                     repeats: true)
        timerAction()
    }

    func stopTimer() {
        // really just pauses the timer
        timer?.invalidate()
        timer = nil
        
        timerAction()
    }

    func resetTimer() {
        // stop the timer and reset it
        timer?.invalidate()
        timer = nil
        startTime = nil
        duration = 360
        elapsedTime = 0
        
        timerAction()
    }
}
